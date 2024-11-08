from homeassistant.components.application_credentials import AuthorizationServer, ClientCredential, AuthImplementation
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_entry_oauth2_flow


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
