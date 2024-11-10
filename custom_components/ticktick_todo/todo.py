""" mqtt-mediaplayer """
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
from .pyticktick.openapi_client import TaskResponse

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
        self._attr_supported_features |= TodoListEntityFeature.DELETE_TODO_ITEM
        self._attr_supported_features |= TodoListEntityFeature.UPDATE_TODO_ITEM
        self._attr_supported_features |= TodoListEntityFeature.SET_DESCRIPTION_ON_ITEM
        self._attr_supported_features |= TodoListEntityFeature.SET_DUE_DATETIME_ON_ITEM

    async def async_update(self):
        """ Update the States"""
        project_data: openapi_client.models.ProjectDataResponse = (
            await self._api_instance.open_v1_project_project_id_data_get(self._id))
        _LOGGER.debug("Project data: %s", project_data)
        self._attr_todo_items = [await TickTickTodo._task_response_to_todo_item(t) for t in project_data.tasks]

    async def async_create_todo_item(self, item: TodoItem) -> None:
        """Add an item to the To-do list."""
        task = await self._api_instance.open_v1_task_post(await TickTickTodo._todo_item_to_task(item))
        _LOGGER.debug("Original task: %s", task)
        task.project_id = self._id
        task.task_id = item.uid
        task_ = await TickTickTodo._task_response_to_task_request(task)
        _LOGGER.debug("Updated task: %s", task_)
        task = await self._api_instance.open_v1_task_task_id_post(item.uid, task_)
        self.todo_items.append(await TickTickTodo._task_response_to_todo_item(task))

    async def async_update_todo_item(self, item: TodoItem) -> None:
        """Add an item to the To-do list."""
        task = await TickTickTodo._merge_todo_item_and_task_response(item,
                                                                     await self._api_instance.open_v1_project_project_id_task_task_id_get(
                                                                         self._id, item.uid))
        task_ = await TickTickTodo._task_response_to_task_request(task)
        await self._api_instance.open_v1_task_task_id_post(task.id, task_)

    async def async_delete_todo_items(self, uids: list[str]) -> None:
        """Delete an item from the to-do list."""
        for uid in uids:
            await self._api_instance.open_v1_project_project_id_task_task_id_delete(self._id, uid)

    @staticmethod
    async def _task_response_to_todo_item(task_response: openapi_client.TaskResponse) -> TodoItem:
        return TodoItem(uid=task_response.id, summary=task_response.title, description=task_response.desc,
                        status=await TickTickTodo._task_status_to_todo_item_status(task_response),
                        due=task_response.due_date)

    @staticmethod
    async def _todo_item_to_task(todo_item: TodoItem) -> openapi_client.Task:
        return openapi_client.Task(id=todo_item.uid, title=todo_item.summary, desc=todo_item.description,
                                   status=await TickTickTodo._todo_item_status_to_task_status(todo_item),
                                   due_date=todo_item.due)

    @staticmethod
    async def _todo_item_to_task_response(todo_item: TodoItem) -> openapi_client.TaskResponse:
        return openapi_client.TaskResponse(id=todo_item.uid, task_id=todo_item.uid, title=todo_item.summary,
                                           desc=todo_item.description,
                                           status=await TickTickTodo._todo_item_status_to_task_status(todo_item),
                                           due_date=todo_item.due)

    @staticmethod
    async def _merge_todo_item_and_task_response(todo_item: TodoItem,
                                                 task_response: TaskResponse) -> openapi_client.TaskResponse:
        task_response.task_id = todo_item.uid
        task_response.status = TickTickTodo._todo_item_status_to_task_status(todo_item)
        task_response.title = todo_item.summary
        task_response.desc = todo_item.description
        task_response.due_date = todo_item.due
        return task_response

    @staticmethod
    async def _task_status_to_todo_item_status(task_response: openapi_client.TaskResponse) -> TodoItemStatus | None:
        if task_response.status == 0:
            return TodoItemStatus.NEEDS_ACTION
        elif task_response.status == 2:
            return TodoItemStatus.COMPLETED
        else:
            return None

    @staticmethod
    async def _todo_item_status_to_task_status(todo_item):
        if todo_item.status == TodoItemStatus.COMPLETED:
            return 2
        elif todo_item.status == TodoItemStatus.NEEDS_ACTION:
            return 0
        else:
            return None

    @staticmethod
    async def _task_response_to_task_request(
            response: openapi_client.TaskResponse) -> openapi_client.OpenV1TaskTaskIdPostRequest:
        return openapi_client.OpenV1TaskTaskIdPostRequest(
            title=response.title,
            is_all_day=response.is_all_day,
            content=response.content,
            desc=response.desc,
            items=response.items,
            priority=response.priority,
            reminders=response.reminders,
            repeat_flag=response.repeat_flag,
            sort_order=response.sort_order,
            start_date=response.start_date,
            time_zone=response.time_zone,
            id=response.id,
            task_id=response.task_id,
            project_id=response.project_id,
            completed_time=response.completed_time,
            status=response.status
        )
