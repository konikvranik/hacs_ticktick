""" mqtt-mediaplayer """
import logging
from datetime import datetime

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.media_player import PLATFORM_SCHEMA, MediaPlayerState
from homeassistant.components.todo import TodoListEntity, TodoItem
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (CONF_NAME, CONF_ACCESS_TOKEN, )
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DOMAIN
from .pyticktick import openapi_client

DOMAIN = DOMAIN
# SCAN_INTERVAL = timedelta(minutes=1)
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


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry,
                            async_add_entities: AddEntitiesCallback) -> None:
    """Set up ESPHome binary sensors based on a config entry."""

    api_instance = hass.data[DOMAIN][config_entry.entry_id]["ticktick_api_instance"]
    # Get User Project.
    async_add_entities([(TickTickTodo(hass, DeviceInfo(name=config_entry.title,
                                                       identifiers={(DOMAIN, config_entry.entry_id)}),
                                      l.id,
                                      l.name,
                                      api_instance
                                      )) for l in (await api_instance.open_v1_project_get())],
                       True)


class TickTickTodo(TodoListEntity):
    """MQTTMediaPlayer"""

    def __init__(self, hass: HomeAssistant, device_info: DeviceInfo, id: str, name: str,
                 api_instance: openapi_client.DefaultApi) -> None:
        """Initialize"""

        self._attr_device_info = device_info
        _LOGGER.debug("TickTickTodo.__init__(%s, %s)" % (id, name))
        self.hass = hass
        self._api_instance = api_instance
        self._id = id
        self._attr_name = name

    async def async_update(self):
        """ Update the States"""
        project_data: openapi_client.models.ProjectDataResponse = (
            await self._api_instance.open_v1_project_project_id_data_get(self._id))
        _LOGGER.debug("Project data: %s", project_data)
        self._attr_todo_items = [
            TodoItem(uid=t.id, summary=t.title, description=t.content, due=t.due_date,
                     status=[homeassistant.components.todo.const.TodoItemStatus.NEEDS_ACTION,
                             homeassistant.components.todo.const.TodoItemStatus.COMPLETED][t.status]) for t in
            project_data.tasks]
