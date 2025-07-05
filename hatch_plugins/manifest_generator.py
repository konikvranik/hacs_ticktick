#!/usr/bin/env python3
"""
Manifest Generator for Home Assistant and HACS

This script generates both the Home Assistant component manifest.json and the HACS hacs.json
from configuration in pyproject.toml.

It can be used as a standalone script or as a Hatch build hook.
"""
import json
import os
import re
from pathlib import Path
from typing import Dict, Any, Optional

def parse_toml(file_path):
    """Simple TOML parser for pyproject.toml

    This is a very basic parser that only handles the specific format
    of pyproject.toml files for this project. It's not a full TOML parser.
    """
    result = {}
    current_section = result
    section_stack = []

    with open(file_path, 'r') as f:
        content = f.read()

    # Remove comments
    content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)

    for line in content.split('\n'):
        line = line.strip()
        if not line:
            continue

        # Section header
        if line.startswith('[') and line.endswith(']'):
            section_path = line[1:-1].split('.')
            current_section = result

            for i, section in enumerate(section_path):
                if section not in current_section:
                    current_section[section] = {}

                if i < len(section_path) - 1:
                    current_section = current_section[section]
                else:
                    section_stack = section_path[:-1]
                    current_section = current_section[section]

        # Key-value pair
        elif '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()

            # Handle string
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            # Handle list
            elif value.startswith('[') and value.endswith(']'):
                value = value[1:-1].split(',')
                value = [v.strip().strip('"') for v in value if v.strip()]
            # Handle boolean
            elif value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            # Handle number
            elif value.isdigit():
                value = int(value)
            elif value.replace('.', '', 1).isdigit():
                value = float(value)

            current_section[key] = value

    return result

class ManifestGenerator:
    """Manifest Generator for Home Assistant and HACS"""

    def __init__(self, directory: Optional[str] = None):
        """Initialize the generator with an optional directory"""
        self.directory = directory or os.getcwd()
        self.pyproject = self.load_pyproject()

    def load_pyproject(self) -> Dict[str, Any]:
        """Load pyproject.toml file"""
        pyproject_path = os.path.join(self.directory, "pyproject.toml")
        return parse_toml(pyproject_path)

    def load_existing_ha_manifest(self, domain: str) -> Dict[str, Any]:
        """Load existing Home Assistant manifest.json if it exists"""
        manifest_path = os.path.join(self.directory, f"custom_components/{domain}/manifest.json")
        if os.path.exists(manifest_path):
            try:
                with open(manifest_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse {manifest_path}, will create a new one")
        return {}

    def generate_ha_manifest(self) -> Dict[str, Any]:
        """Update Home Assistant manifest.json with selected fields from pyproject.toml"""
        ha_config = self.pyproject.get("tool", {}).get("homeassistant", {})

        # Get domain from pyproject.toml or try to find it from existing manifest files
        domain = ha_config.get("domain")
        if not domain:
            # Look for existing manifest files in custom_components directory
            custom_components_dir = os.path.join(self.directory, "custom_components")
            if os.path.exists(custom_components_dir):
                for component_dir in os.listdir(custom_components_dir):
                    manifest_path = os.path.join(custom_components_dir, component_dir, "manifest.json")
                    if os.path.exists(manifest_path):
                        try:
                            with open(manifest_path, 'r') as f:
                                manifest_data = json.load(f)
                                if "domain" in manifest_data:
                                    domain = manifest_data["domain"]
                                    break
                        except json.JSONDecodeError:
                            pass

        # If still no domain found, use "unknown"
        if not domain:
            domain = "unknown"

        # Load existing manifest
        manifest = self.load_existing_ha_manifest(domain)

        # Set name from project.name
        if "name" in self.pyproject.get("project", {}):
            manifest["name"] = self.pyproject["project"]["name"]

        # Only update specific fields from pyproject.toml
        # Do not update: version, codeowners, documentation, issue_tracker, requirements
        # Note: name is updated from project.name, not from tool.homeassistant
        updateable_fields = [
            "domain",
            "dependencies",
            "config_flow",
            "iot_class",
            "integration_type",
            "icon",
            "logo"
        ]

        # Update only the allowed fields
        for field in updateable_fields:
            if field in ha_config:
                manifest[field] = ha_config[field]

        return manifest

    def load_existing_hacs_manifest(self) -> Dict[str, Any]:
        """Load existing HACS hacs.json if it exists"""
        manifest_path = os.path.join(self.directory, "hacs.json")
        if os.path.exists(manifest_path):
            try:
                with open(manifest_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse {manifest_path}, will create a new one")
        return {}

    def generate_hacs_manifest(self) -> Dict[str, Any]:
        """Generate HACS hacs.json with name from project.name"""
        # Load existing manifest
        manifest = self.load_existing_hacs_manifest()

        # Set name from project.name
        if "name" in self.pyproject.get("project", {}):
            manifest["name"] = self.pyproject["project"]["name"]

        return manifest

    def save_ha_manifest(self, manifest: Dict[str, Any], domain: str):
        """Save Home Assistant manifest.json"""
        manifest_path = os.path.join(self.directory, f"custom_components/{domain}/manifest.json")
        os.makedirs(os.path.dirname(manifest_path), exist_ok=True)

        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)

        print(f"✅ Updated {manifest_path} with fields from pyproject.toml")
        print("   (name is set from project.name)")
        print("   (preserved version, codeowners, documentation, issue_tracker, requirements)")

    def save_hacs_manifest(self, manifest: Dict[str, Any]):
        """Save HACS hacs.json"""
        manifest_path = os.path.join(self.directory, "hacs.json")

        # Always save the manifest to update the name field
        if manifest:
            with open(manifest_path, "w") as f:
                json.dump(manifest, f, indent=2)
            if os.path.exists(manifest_path):
                print(f"✅ Updated {manifest_path} with name from project.name")
            else:
                print(f"✅ Created {manifest_path}")
        else:
            print(f"ℹ️ No manifest data to save to {manifest_path}")

    def generate_all(self):
        """Generate and save manifest files"""
        print("🔄 Manifest Generator")
        print("   - Updating name field from project.name in both manifest files")
        print("   - Also updating specific fields in manifest.json")

        # Update Home Assistant manifest
        ha_manifest = self.generate_ha_manifest()
        if ha_manifest:
            self.save_ha_manifest(ha_manifest, ha_manifest.get("domain", "unknown"))

        # Preserve HACS manifest (only create if it doesn't exist)
        hacs_manifest = self.generate_hacs_manifest()
        self.save_hacs_manifest(hacs_manifest)

# Hatch hook interface
def hook(directory):
    """Hatch build hook to generate manifest files"""
    generator = ManifestGenerator(directory)
    generator.generate_all()

# Standalone script interface
def main():
    """Main function when run as a standalone script"""
    generator = ManifestGenerator()
    generator.generate_all()

if __name__ == "__main__":
    main()
