""" mqtt-mediaplayer """
import datetime
import logging

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.media_player import PLATFORM_SCHEMA, MediaPlayerState
from homeassistant.components.todo import (
    TodoItemStatus,
    TodoListEntityFeature
)
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
    projects_ = await api_instance.open_v1_project_get()
    async_add_entities([(TickTickTodo(hass, DeviceInfo(name=config_entry.title,
                                                       identifiers={(DOMAIN, config_entry.entry_id)}),
                                      l.id,
                                      l.name,
                                      api_instance
                                      )) for l in projects_],
                       False)


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
        self._attr_supported_features = TodoListEntityFeature.CREATE_TODO_ITEM
        # self._attr_supported_features |= TodoListEntityFeature.DELETE_TODO_ITEM
        # self._attr_supported_features |= TodoListEntityFeature.UPDATE_TODO_ITEM
        self._attr_supported_features |= TodoListEntityFeature.SET_DESCRIPTION_ON_ITEM
        self._attr_supported_features |= TodoListEntityFeature.SET_DUE_DATETIME_ON_ITEM

    async def async_update(self):
        """ Update the States"""
        project_data: openapi_client.models.ProjectDataResponse = (
            await self._api_instance.open_v1_project_project_id_data_get(self._id))
        _LOGGER.debug("Project data: %s", project_data)
        self._attr_todo_items = [TickTickTodoItem(t) for t in project_data.tasks]

    async def async_create_todo_item(self, item: TodoItem) -> None:
        """Add an item to the To-do list."""
        await self._api_instance.open_v1_task_post(TickTickTask(item))


class TickTickTodoItem(TodoItem, openapi_client.TaskResponse):

    def __init__(self, task_response: openapi_client.TaskResponse):
        super().__init__()
        self._task_response = task_response

    @property
    def task_response(self):
        return self._task_response

    @property
    def summary(self) -> str:
        return self._task_response.title

    @summary.setter
    def summary(self, summary: str):
        self._task_response.title = summary

    @property
    def status(self) -> TodoItemStatus:
        if self._task_response.status == 0:
            return TodoItemStatus.COMPLETED
        elif self._task_response.status == 2:
            return TodoItemStatus.NEEDS_ACTION
        else:
            return None

    @status.setter
    def status(self, status: TodoItemStatus):
        if status == TodoItemStatus.COMPLETED:
            self._task_response.status = 0
        elif status == TodoItemStatus.NEEDS_ACTION:
            self._task_response.status = 2
        else:
            self._task_response.status = None

    @property
    def due(self):
        return self._task_response.due_date

    @due.setter
    def due(self, due_date: datetime.datetime):
        self._task_response.due_date = due_date

    @property
    def description(self):
        return self._task_response.desc

    @description.setter
    def description(self, description: str):
        self._task_response.desc = description

    @property
    def uid(self):
        return self._task_response.id

    @uid.setter
    def uid(self, uuid: str):
        self._task_response.id = uuid


class TickTickTask(openapi_client.Task):

    def __init__(self, item: TodoItem) -> None:
        super().__init__()
        self._todo_item = item

    @property
    def id(self):
        return self._todo_item.uid

    @id.setter
    def id(self, id: str):
        self._todo_item.uid = id

    @property
    def title(self):
        return self._todo_item.summary

    @title.setter
    def title(self, title: str):
        self._todo_item.summary = title

    @property
    def desc(self):
        return self._todo_item.description

    @desc.setter
    def desc(self, desc: str):
        self._todo_item.description = desc

    @property
    def due_date(self):
        return self._todo_item.due

    @due_date.setter
    def due_date(self, due_date: datetime.datetime):
        self._todo_item.due = due_date

    @property
    def status(self):
        if self._todo_item.status == TodoItemStatus.COMPLETED:
            return 0
        elif self._todo_item.status == TodoItemStatus.NEEDS_ACTION:
            return 2
        else:
            return None

    @status.setter
    def status(self, status: int):
        if status == 0:
            self._todo_item.status = TodoItemStatus.COMPLETED
        elif status == 2:
            self._todo_item.status == TodoItemStatus.NEEDS_ACTION
