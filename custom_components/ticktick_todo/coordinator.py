import asyncio
import logging
from datetime import timedelta

import async_timeout
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from custom_components.ticktick_todo.pyticktick import openapi_client
from custom_components.ticktick_todo.pyticktick.openapi_client import ProjectData

_LOGGER = logging.getLogger(__name__)


class TicktickUpdateCoordinator(DataUpdateCoordinator[dict[str, ProjectData]]):
    """HKO Update Coordinator."""

    def __init__(self, hass, api_client: openapi_client.ApiClient):
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
            always_update=True
        )
        self._api_instance = openapi_client.DefaultApi(api_client)

    async def _async_setup(self):
        """Set up the coordinator

        This is the place to set up your coordinator,
        or to load data, that only needs to be loaded once.

        This method will be called automatically during
        coordinator.async_config_entry_first_refresh.
        """
        projects_ = await self._api_instance.open_v1_project_get()
        self.data = {p.id: ProjectData(project=p) for p in projects_}

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

            result = dict()
            #for idx in listening_idx:
            for idx in self.data.keys():
                project_data: openapi_client.models.ProjectData = (
                    await self._api_instance.open_v1_project_project_id_data_get(idx))
                _LOGGER.debug("Project data: %s", project_data)
                result[project_data.project.id] = project_data
                asyncio.timeout(.7)

            return result
