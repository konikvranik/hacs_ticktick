import asyncio
import logging
from datetime import timedelta

import async_timeout
import pyticktick
from homeassistant.components.todo import TodoItem
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from pyticktick.exceptions import ApiException
from pyticktick.models import ProjectData

from custom_components.ticktick_todo.helper import TaskMapper

_LOGGER = logging.getLogger(__name__)


class TicktickUpdateCoordinator(DataUpdateCoordinator[dict[str, ProjectData]]):
    """HKO Update Coordinator."""

    def __init__(self, hass, _config_entry: ConfigEntry, token: str):
        """Initialize my coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            # Name of the data. For logging purposes.
            name="TickTick TODO",
            # Polling interval. Will only be polled if there are subscribers.
            update_interval=timedelta(seconds=30),
        )
        self._api_instance = pyticktick.DefaultApi(pyticktick.ApiClient(pyticktick.Configuration(access_token=token)))
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
                    if self.data is None:
                        self.data = {}
                    projects_ = await self._api_instance.get_all_projects()
                    result = {k.id: self.data.setdefault(k.id, ProjectData(project=k)) for k in projects_}

                    for idx in result:
                        if idx in listening_idx or result[idx].tasks is None:
                            project_data: pyticktick.models.ProjectData = (
                                await self._api_instance.get_project_with_data_by_id(idx)
                            )
                            _LOGGER.debug("Project data: %s", project_data)
                            result[project_data.project.id] = project_data
                except ApiException as err:
                    raise UpdateFailed(f"Error communicating with API: {err}") from err
                except Exception as err:
                    raise UpdateFailed(f"Error communicating with API: {err}") from err
            return result

    async def async_create_todo_item(self, project_id: str, item: TodoItem) -> TodoItem:
        """Add an item to the To-do list."""
        _LOGGER.debug("Source item: %s", item)
        async with self._api_call_lock:
            current_task_ = await self._api_instance.create_single_task(TaskMapper.todo_item_to_task(project_id, item))
        item.uid = current_task_.id
        await self.async_request_refresh()
        return item

    async def async_update_todo_item(self, project_id: str, item: TodoItem) -> None:
        """Add an item to the To-do list."""
        async with self._api_call_lock:
            await self._api_instance.complete_specify_task_with_http_info
            project_data = await self._api_instance.get_project_with_data_by_id(project_id)
            for t in project_data.tasks:
                if t.id == item.uid:
                    task = TaskMapper.merge_todo_item_and_task_response(item, t)
                    task_ = TaskMapper.task_response_to_task_request(task)
                    await self._api_instance.delete_specify_task(project_id, t.id)
                    await self._api_instance.create_single_task(task_)
                    await self.async_request_refresh()
                    return

    async def async_delete_todo_items(self, project_id: str, uids: list[str]) -> None:
        """Delete an item from the to-do list."""
        async with self._api_call_lock:
            for uid in uids:
                await self._api_instance.delete_specify_task(project_id, uid)
        await self.async_request_refresh()
