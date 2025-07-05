# Manifest Generator for Home Assistant and HACS

This directory contains a Hatch plugin that selectively updates the Home Assistant manifest file based on configuration in `pyproject.toml` while preserving HACS-specific information.

## Features

- Updates specific fields in `custom_components/ticktick_todo/manifest.json` from `pyproject.toml`
- Preserves important fields in manifest.json (version, name, codeowners, documentation, issue_tracker, requirements)
- Preserves the existing `hacs.json` file without modifications
- Runs automatically during the build process
- Can also be run manually

## Configuration

The manifest generator uses configuration from the `[tool.homeassistant]` section in `pyproject.toml` to update specific fields in the manifest.json file.

### Fields Updated from pyproject.toml

Only the following fields are updated from `pyproject.toml`:

```toml
[tool.homeassistant]
domain = "ticktick_todo"       # Updated in manifest.json
dependencies = [...]           # Updated in manifest.json
config_flow = true             # Updated in manifest.json
iot_class = "cloud_polling"    # Updated in manifest.json
icon = "..."                   # Updated in manifest.json
logo = "..."                   # Updated in manifest.json
```

### Fields Preserved in manifest.json

The following fields are preserved from the existing manifest.json file and NOT updated from pyproject.toml:

- `version`
- `name`
- `codeowners`
- `documentation` (URL)
- `issue_tracker` (URL)
- `requirements`

### HACS Configuration

The `hacs.json` file is preserved without any modifications. The `[tool.hacs]` section in `pyproject.toml` is not used by this generator.

## Usage

### Automatic Generation

The manifest.json file is automatically updated during the build process thanks to the following configuration in `pyproject.toml`:

```toml
[tool.hatch.build.hooks.custom]
path = "hatch_plugins/manifest_generator.py"
```

### Manual Generation

You can also run the script manually:

```bash
python hatch_plugins/manifest_generator.py
```

This will:
1. Update specific fields in manifest.json from pyproject.toml
2. Preserve important fields in manifest.json (version, name, codeowners, documentation, issue_tracker, requirements)
3. Leave the existing hacs.json file unchanged

### Output Example

When you run the script, you'll see output similar to:

```
🔄 Manifest Generator
   - Only updating specific fields in manifest.json
   - Preserving all HACS-specific information in hacs.json
✅ Updated custom_components/ticktick_todo/manifest.json with fields from pyproject.toml
   (preserved version, name, codeowners, documentation, issue_tracker, requirements)
ℹ️ Preserved existing hacs.json without changes
```
