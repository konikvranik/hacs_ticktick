"""Fixtures for TickTick TODO tests."""

import sys
from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo

# Mock the pyticktick module before importing our components
# Create mock modules
mock_pyticktick = MagicMock()
mock_pyticktick.exceptions = MagicMock()
mock_pyticktick.exceptions.ApiException = type("MockApiException", (Exception,), {})
mock_pyticktick.models = MagicMock()
mock_pyticktick.models.ProjectData = type(
    "MockProjectData",
    (),
    {
        "__init__": lambda self, project=None, tasks=None: (
            setattr(self, "project", project) or setattr(self, "tasks", tasks)
        )
    },
)

# Add mock modules to sys.modules
sys.modules["pyticktick"] = mock_pyticktick
sys.modules["pyticktick.exceptions"] = mock_pyticktick.exceptions
sys.modules["pyticktick.models"] = mock_pyticktick.models

from custom_components.ticktick_todo import DOMAIN  # noqa: E402
from custom_components.ticktick_todo.coordinator import TicktickUpdateCoordinator  # noqa: E402


@pytest.fixture
def mock_hass():
    """Return a mocked HomeAssistant instance."""
    return MagicMock(spec=HomeAssistant)


@pytest.fixture
def mock_config_entry():
    """Return a mocked ConfigEntry instance."""
    config_entry = MagicMock(spec=ConfigEntry)
    config_entry.title = "Test TickTick"
    config_entry.entry_id = "test_entry_id"
    return config_entry


@pytest.fixture
def mock_api_instance():
    """Return a mocked API instance."""
    mock = MagicMock()
    mock.get_all_projects = AsyncMock()
    mock.get_project_with_data_by_id = AsyncMock()
    mock.create_single_task = AsyncMock()
    mock.delete_specify_task = AsyncMock()
    return mock


@pytest.fixture
def mock_device_info():
    """Return a mocked DeviceInfo instance."""
    return DeviceInfo(name="Test Device", identifiers={(DOMAIN, "test_entry_id")})


@pytest.fixture
def mock_coordinator():
    """Return a mocked coordinator instance."""
    coordinator = MagicMock(spec=TicktickUpdateCoordinator)

    # Mock async methods
    coordinator.async_create_todo_item = AsyncMock()
    coordinator.async_config_entry_first_refresh = AsyncMock()
    coordinator.async_refresh = AsyncMock()

    # Mock project data
    project1 = MagicMock()
    project1.name = "Project 1"

    project2 = MagicMock()
    project2.name = "Project 2"

    # Mock tasks
    task1 = MagicMock()
    task1.id = "task1"
    task1.title = "Task 1"

    task2 = MagicMock()
    task2.id = "task2"
    task2.title = "Task 2"

    # Set up coordinator data
    coordinator.data = {
        "project1": MagicMock(project=project1, tasks=[task1]),
        "project2": MagicMock(project=project2, tasks=[task2]),
    }

    return coordinator
