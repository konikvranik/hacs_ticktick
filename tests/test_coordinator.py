"""Test the TickTick TODO coordinator."""

from unittest.mock import MagicMock, patch

import pytest
from homeassistant.components.todo import TodoItem
from homeassistant.helpers.update_coordinator import UpdateFailed
from pyticktick.exceptions import ApiException
from pyticktick.models import ProjectData

from custom_components.ticktick_todo.coordinator import TicktickUpdateCoordinator


@pytest.fixture
def coordinator(mock_hass, mock_config_entry, mock_api_instance):
    """Return a coordinator with mocked API."""
    with patch("pyticktick.DefaultApi", return_value=mock_api_instance), patch("pyticktick.ApiClient"), patch(
        "pyticktick.Configuration"
    ):
        coordinator = TicktickUpdateCoordinator(mock_hass, mock_config_entry, "test_token")
        coordinator.data = {}
        return coordinator


@pytest.mark.anyio
async def test_async_update_data(coordinator, mock_api_instance):
    """Test the _async_update_data method."""
    # Setup
    project = MagicMock()
    project.id = "project1"
    mock_api_instance.get_all_projects.return_value = [project]

    project_data = MagicMock(spec=ProjectData)
    project_data.project = project
    mock_api_instance.get_project_with_data_by_id.return_value = project_data

    # Test
    result = await coordinator._async_update_data()

    # Verify
    assert "project1" in result
    assert result["project1"] == project_data
    assert mock_api_instance.get_all_projects.called
    assert mock_api_instance.get_project_with_data_by_id.called


@pytest.mark.anyio
async def test_async_update_data_api_exception(coordinator, mock_api_instance):
    """Test the _async_update_data method with API exception."""
    # Setup
    mock_api_instance.get_all_projects.side_effect = ApiException("API error")

    # Test & Verify
    with pytest.raises(UpdateFailed):
        await coordinator._async_update_data()


@pytest.mark.anyio
async def test_async_create_todo_item(coordinator, mock_api_instance):
    """Test the async_create_todo_item method."""
    # Setup
    item = MagicMock(spec=TodoItem)
    task = MagicMock()
    task.id = "task1"
    mock_api_instance.create_single_task.return_value = task

    with patch("custom_components.ticktick_todo.helper.TaskMapper.todo_item_to_task") as mock_to_task:
        # Test
        result = await coordinator.async_create_todo_item("project1", item)

        # Verify
        assert result == item
        assert item.uid == "task1"
        assert mock_to_task.called
        assert mock_api_instance.create_single_task.called
