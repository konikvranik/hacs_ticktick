"""Test the TickTick TODO integration initialization."""
import pytest
from unittest.mock import patch, MagicMock

from custom_components.ticktick_todo import (
    async_setup,
    async_setup_entry,
    async_unload_entry,
    async_migrate_entry,
    DOMAIN,
    PLATFORMS,
)


@pytest.mark.anyio
async def test_setup(mock_hass):
    """Test the setup function."""
    config = {}

    result = await async_setup(mock_hass, config)

    assert result is True


@pytest.mark.anyio
async def test_setup_entry(mock_hass, mock_config_entry):
    """Test the setup entry function."""
    with patch("custom_components.ticktick_todo._get_valid_token", return_value="test_token"), \
         patch("custom_components.ticktick_todo.TicktickUpdateCoordinator") as mock_coordinator:

        mock_coordinator_instance = mock_coordinator.return_value
        mock_coordinator_instance.async_config_entry_first_refresh = MagicMock()

        result = await async_setup_entry(mock_hass, mock_config_entry)

        assert result is True
        assert mock_config_entry.runtime_data["coordinator"] == mock_coordinator_instance
        assert mock_hass.config_entries.async_forward_entry_setups.called_with(mock_config_entry, PLATFORMS)


@pytest.mark.anyio
async def test_unload_entry(mock_hass, mock_config_entry):
    """Test the unload entry function."""
    mock_hass.config_entries.async_unload_platforms.return_value = True

    result = await async_unload_entry(mock_hass, mock_config_entry)

    assert result is True
    assert mock_hass.config_entries.async_unload_platforms.called_with(mock_config_entry, PLATFORMS)


@pytest.mark.anyio
async def test_migrate_entry(mock_hass, mock_config_entry):
    """Test the migrate entry function."""
    result = await async_migrate_entry(mock_hass, mock_config_entry)

    assert result is True
