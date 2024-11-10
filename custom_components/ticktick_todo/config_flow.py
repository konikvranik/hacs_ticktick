"""Adds config flow for HDO."""
import datetime
import logging
import time
from pathlib import Path
from typing import Any, Mapping

from homeassistant.config_entries import ConfigFlowResult, SOURCE_REAUTH
from homeassistant.helpers import config_entry_oauth2_flow

from . import DOMAIN, DEBUG

_LOGGER = logging.getLogger(__name__)


class TicktickFlowHandler(config_entry_oauth2_flow.AbstractOAuth2FlowHandler, domain=DOMAIN):
    """Config flow to handle Netatmo OAuth2 authentication."""

    DOMAIN = DOMAIN

    @property
    def logger(self) -> logging.Logger:
        """Return logger."""
        return logging.getLogger(__name__)

    @property
    def extra_authorize_data(self) -> dict:
        """Extra data that needs to be appended to the authorize url."""
        return {"scope": " ".join(["tasks:write", "tasks:read"])}

    async def async_step_user(self, user_input: dict | None = None) -> ConfigFlowResult:
        """Handle a flow start."""

        if DEBUG:
            return self.async_create_entry(
                title="Title of the entry",
                data={
                    "token": {"access_token": self.hass.async_add_executor_job( open, f'{Path.home()}/.ticktick_token'), "expires_at": time.time() + datetime.timedelta(days=365).seconds},
                },
                options={
                },
            )

        await self.async_set_unique_id(DOMAIN)

        if (self.source !=
                SOURCE_REAUTH and self._async_current_entries()):
            return self.async_abort(reason="single_instance_allowed")

        return await super().async_step_user(user_input)

    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult:
        """Perform reauth upon an API authentication error."""
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(self, user_input: dict | None = None) -> ConfigFlowResult:
        """Dialog that informs the user that reauth is required."""
        if user_input is None:
            return self.async_show_form(step_id="reauth_confirm")

        return await self.async_step_user()

    async def async_oauth_create_entry(self, data: dict) -> ConfigFlowResult:
        """Create an oauth config entry or update existing entry for reauth."""
        existing_entry = await self.async_set_unique_id(DOMAIN)
        if existing_entry:
            self.hass.config_entries.async_update_entry(existing_entry, data=data)
            await self.hass.config_entries.async_reload(existing_entry.entry_id)
            return self.async_abort(reason="reauth_successful")

        return await super().async_oauth_create_entry(data)
