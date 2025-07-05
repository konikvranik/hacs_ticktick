"""mqtt-mediaplayer"""

import logging

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.media_player import PLATFORM_SCHEMA, MediaPlayerState
from homeassistant.components.todo import TodoItem, TodoListEntity, TodoListEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN, CONF_NAME
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import DOMAIN, SCAN_INTERVAL, TicktickUpdateCoordinator
from .helper import TaskMapper

DOMAIN = DOMAIN
SCAN_INTERVAL = SCAN_INTERVAL
_LOGGER = logging.getLogger(__name__)
_VALID_STATES = [
    MediaPlayerState.ON,
    MediaPlayerState.OFF,
    "true",
    "false",
]

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Required(CONF_ACCESS_TOKEN): cv.string,
    }
)


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up ESPHome binary sensors based on a config entry."""
    coordinator = config_entry.runtime_data["coordinator"]
    new_entities_ = [
        TickTickTodo(
            hass, DeviceInfo(name=config_entry.title, identifiers={(DOMAIN, config_entry.entry_id)}), coordinator, id
        )
        for id in coordinator.data.keys()
    ]
    async_add_entities(new_entities_)


class TickTickTodo(CoordinatorEntity[TicktickUpdateCoordinator], TodoListEntity):
    """MQTTMediaPlayer"""

    def __init__(
        self, hass: HomeAssistant, device_info: DeviceInfo, coordinator: TicktickUpdateCoordinator, id: str
    ) -> None:
        """Initialize"""

        super().__init__(coordinator, context=id)
        self._ticktick_project_id = id
        self._attr_name = coordinator.data[id].project.name
        self._attr_device_info = device_info
        _LOGGER.debug("TickTickTodo.__init__(%s, %s)" % (self._ticktick_project_id, self._attr_name))
        self.hass = hass
        self._attr_supported_features = TodoListEntityFeature.CREATE_TODO_ITEM
        self._attr_supported_features |= TodoListEntityFeature.DELETE_TODO_ITEM
        self._attr_supported_features |= TodoListEntityFeature.UPDATE_TODO_ITEM
        self._attr_supported_features |= TodoListEntityFeature.SET_DESCRIPTION_ON_ITEM
        self._attr_supported_features |= TodoListEntityFeature.SET_DUE_DATETIME_ON_ITEM

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_todo_items = [
            TaskMapper.task_to_todo_item(t) for t in self.coordinator.data[self._ticktick_project_id].tasks
        ]
        self.async_write_ha_state()

    def get_unique_id(self) -> str:
        return f"ticktickt_todo_list_{self._ticktick_project_id}"

    async def async_create_todo_item(self, item: TodoItem) -> None:
        """Add an item to the To-do list."""
        _LOGGER.debug("Source item: %s", item)
        self.todo_items.append(await self.coordinator.async_create_todo_item(self._ticktick_project_id, item))

    async def async_update_todo_item(self, item: TodoItem) -> None:
        """Add an item to the To-do list."""
        await self.coordinator.async_update_todo_item(self._ticktick_project_id, item)

    async def async_delete_todo_items(self, uids: list[str]) -> None:
        """Delete an item from the to-do list."""
        await self.coordinator.async_delete_todo_items(self._ticktick_project_id, uids)
