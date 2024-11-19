import asyncio
import logging
from datetime import timedelta

import async_timeout
from homeassistant.components.todo import TodoItem
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from custom_components.ticktick_todo.helper import TaskMapper
from custom_components.ticktick_todo.pyticktick import openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client import ProjectData, ApiException

_LOGGER = logging.getLogger(__name__)


class TicktickUpdateCoordinator(DataUpdateCoordinator[dict[str, ProjectData]]):
    """HKO Update Coordinator."""

    def __init__(self, hass, config_entry: ConfigEntry, token: str):
        """Initialize my coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            # Name of the data. For logging purposes.
            name="TickTick TODO",
            # Polling interval. Will only be polled if there are subscribers.
            update_interval=timedelta(seconds=30),
            # Set always_update to `False` if the data returned from the
            # api can be compared via `__eq__` to avoid duplicate updates
            # being dispatched to listeners
            always_update=False,
            config_entry=config_entry
        )
        api_client = openapi_client.ApiClient(openapi_client.Configuration(access_token=token))
        self._api_instance = openapi_client.DefaultApi(api_client)
        self._api_call_lock = asyncio.Lock()

    async def _async_setup(self):
        """Set up the coordinator

        This is the place to set up your coordinator,
        or to load data, that only needs to be loaded once.

        This method will be called automatically during
        coordinator.async_config_entry_first_refresh.
        """

        # async with self._api_call_lock:
        #     projects_ = await self._api_instance.open_v1_project_get()
        #
        # self.data = {p.id: ProjectData(project=p) for p in projects_}

    async def _async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        # Note: asyncio.TimeoutError and aiohttp.ClientError are already
        # handled by the data update coordinator.
        async with async_timeout.timeout(10):
            # Grab active context variables to limit data required to be fetched from API
            # Note: using context is not required if there is no need or ability to limit
            # data retrieved from API.
            listening_idx = set(self.async_contexts())
            _LOGGER.debug("Listening contexts: %s", listening_idx)

            async with self._api_call_lock:
                try:
                    projects_ = await self._api_instance.open_v1_project_get()
                    result = {k.id: self.data.setdefault(k.id, ProjectData(project=k)) for k in projects_}
                    asyncio.timeout(1)

                    for idx in result.keys():

                        if idx in listening_idx or result[idx].tasks is None:
                            project_data: openapi_client.models.ProjectData = (
                                await self._api_instance.open_v1_project_project_id_data_get(idx))
                            _LOGGER.debug("Project data: %s", project_data)
                            result[project_data.project.id] = project_data
                            asyncio.timeout(1)
                except ApiException as err:
                    raise UpdateFailed(f"Error communicating with API: {err}")
            return result

    async def async_create_todo_item(self, project_id: str, item: TodoItem) -> TodoItem:
        """Add an item to the To-do list."""
        _LOGGER.debug("Source item: %s", item)
        async with self._api_call_lock:
            current_task_ = await self._api_instance.open_v1_task_post(
                TaskMapper.todo_item_to_task(project_id, item))
        item.uid = current_task_.id
        asyncio.timeout(1)
        await self.async_request_refresh()
        return item

    async def async_update_todo_item(self, project_id: str, item: TodoItem) -> None:
        """Add an item to the To-do list."""
        async with self._api_call_lock:
            task = TaskMapper.merge_todo_item_and_task_response(item,
                                                                await self._api_instance.open_v1_project_project_id_task_task_id_get(
                                                                    project_id, item.uid))
        task_ = TaskMapper.task_response_to_task_request(task)
        await self._api_instance.open_v1_task_task_id_post(task.id, task_)
        asyncio.timeout(1)
        await self.async_request_refresh()

    async def async_delete_todo_items(self, project_id: str, uids: list[str]) -> None:
        """Delete an item from the to-do list."""
        with self._api_call_lock:
            for uid in uids:
                await self._api_instance.open_v1_project_project_id_task_task_id_delete(project_id, uid)
        asyncio.timeout(1)
        await self.async_request_refresh()
