"""Test the TickTick TODO todo platform."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from homeassistant.components.todo import TodoItem

from custom_components.ticktick_todo.todo import TickTickTodo, async_setup_entry


@pytest.mark.anyio
async def test_async_setup_entry(mock_hass, mock_config_entry, mock_coordinator):
    """Test the async_setup_entry function."""
    # Setup
    mock_config_entry.runtime_data = {"coordinator": mock_coordinator}
    async_add_entities = MagicMock()

    # Test
    await async_setup_entry(mock_hass, mock_config_entry, async_add_entities)

    # Verify
    async_add_entities.assert_called_once()
    # Check that we created entities for each project
    assert len(async_add_entities.call_args[0][0]) == 2


@pytest.mark.anyio
async def test_tickticktodo_init(mock_hass, mock_coordinator, mock_device_info):
    """Test the TickTickTodo initialization."""
    # Setup

    # Test
    todo = TickTickTodo(mock_hass, mock_device_info, mock_coordinator, "project1")

    # Verify
    assert todo.name == "Project 1"
    assert todo.device_info == mock_device_info
    assert todo._ticktick_project_id == "project1"


@pytest.mark.anyio
async def test_tickticktodo_handle_coordinator_update(mock_hass, mock_coordinator, mock_device_info):
    """Test the _handle_coordinator_update method."""
    # Setup
    todo = TickTickTodo(mock_hass, mock_device_info, mock_coordinator, "project1")

    with patch(
        "custom_components.ticktick_todo.helper.TaskMapper.task_to_todo_item"
    ) as mock_to_todo_item, patch.object(todo, "async_write_ha_state") as mock_write_ha_state:
        mock_to_todo_item.return_value = MagicMock(spec=TodoItem)

        # Test
        todo._handle_coordinator_update()

        # Verify
        assert mock_to_todo_item.called
        assert mock_write_ha_state.called


@pytest.mark.anyio
async def test_tickticktodo_async_create_todo_item(mock_hass, mock_coordinator, mock_device_info):
    """Test the async_create_todo_item method."""
    # Setup
    todo = TickTickTodo(mock_hass, mock_device_info, mock_coordinator, "project1")
    item = MagicMock(spec=TodoItem)

    mock_coordinator.async_create_todo_item = AsyncMock(return_value=item)

    # Test
    await todo.async_create_todo_item(item)

    # Verify
    mock_coordinator.async_create_todo_item.assert_called_with("project1", item)
