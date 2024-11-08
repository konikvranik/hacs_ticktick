from json import JSONDecodeError
from typing import cast

from aiohttp import ClientError
from homeassistant.components.application_credentials import AuthorizationServer, ClientCredential, AuthImplementation
from homeassistant.core import HomeAssistant, _LOGGER
from homeassistant.helpers import config_entry_oauth2_flow, http
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import MY_AUTH_CALLBACK_PATH, HEADER_FRONTEND_BASE, \
    AUTH_CALLBACK_PATH
from homeassistant.util import aiohttp


async def async_get_auth_implementation(
        hass: HomeAssistant, auth_domain: str, credential: ClientCredential
) -> config_entry_oauth2_flow.AbstractOAuth2Implementation:
    """Return auth implementation for a custom auth implementation."""
    return TickTickAuthImplementation(
        hass,
        auth_domain,
        credential,
        AuthorizationServer(
            authorize_url="https://ticktick.com/oauth/authorize",
            token_url="https://ticktick.com/oauth/token"
        )
    )


class TickTickAuthImplementation(AuthImplementation):

    @property
    def extra_authorize_data(self) -> dict:
        """Extra data that needs to be appended to the authorize url."""
        return {
            "scope": "tasks:write tasks:read"
        }

    @property
    def redirect_uri(self) -> str:
        """Return the redirect uri."""
        if "my" in self.hass.config.components:
            return MY_AUTH_CALLBACK_PATH

        if (req := http.current_request.get()) is None:
            raise RuntimeError("No current request in context")

        if (ha_host := req.headers.get(HEADER_FRONTEND_BASE)) is None:
            raise RuntimeError("No header in request")

        return f"{ha_host}{AUTH_CALLBACK_PATH}"

    async def _token_request(self, data: dict) -> dict:
        """Make a token request."""
        session = async_get_clientsession(self.hass)

        data["scope"] = "tasks:write tasks:read"

        _LOGGER.debug("Sending token request to %s", self.token_url)
        resp = await session.post(self.token_url, data=data,auth=aiohttp.BasicAuth(self.client_id, self.client_secret))
        if resp.status >= 400:
            try:
                error_response = await resp.json()
            except (ClientError, JSONDecodeError):
                error_response = {}
            error_code = error_response.get("error", "unknown")
            error_description = error_response.get("error_description", "unknown error")
            _LOGGER.error(
                "Token request for %s failed (%s): %s",
                self.domain,
                error_code,
                error_description,
            )
        resp.raise_for_status()
        return cast(dict, await resp.json())
