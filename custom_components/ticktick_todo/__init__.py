import json
import logging
import os
from http import HTTPStatus

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from aiohttp import ClientResponseError
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (CONF_NAME, CONF_FORCE_UPDATE, CONF_HOST, Platform, CONF_DOMAIN,
                                 CONF_ACCESS_TOKEN)
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from homeassistant.helpers import config_entry_oauth2_flow, aiohttp_client
from homeassistant.util import aiohttp
from voluptuous import ALLOW_EXTRA

_LOGGER = logging.getLogger(__name__)
_LOGGER.info('Starting tictick_todo')

MANIFEST = json.load(open("%s/manifest.json" % os.path.dirname(os.path.realpath(__file__))))
VERSION = MANIFEST["version"]
DOMAIN = MANIFEST[CONF_DOMAIN]
DEFAULT_NAME = MANIFEST[CONF_NAME]
PLATFORMS = [Platform.TODO]
ISSUE_URL = "https://github.com/konikvranik/hacs_ticktick/issues"

SCHEMA = {
    vol.Required(CONF_HOST): cv.string,
    vol.Required(CONF_ACCESS_TOKEN): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_FORCE_UPDATE, default=True): cv.boolean,
}

CONFIG_SCHEMA = vol.Schema({vol.Optional(DOMAIN): vol.Schema(SCHEMA)}, extra=ALLOW_EXTRA)


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up ESPHome binary sensors based on a config entry."""

    implementation = (
        await config_entry_oauth2_flow.async_get_config_entry_implementation(
            hass, config_entry
        )
    )

    # Set unique id if non was set (migration)
    if not config_entry.unique_id:
        hass.config_entries.async_update_entry(config_entry, unique_id=DOMAIN)

    session = config_entry_oauth2_flow.OAuth2Session(hass, config_entry, implementation)

    try:
        await session.async_ensure_token_valid()
    except ClientResponseError as ex:
        _LOGGER.warning("API error: %s (%s)", ex.status, ex.message)
        if ex.status in (
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNAUTHORIZED,
                HTTPStatus.FORBIDDEN,
        ):
            raise ConfigEntryAuthFailed("Token not valid, trigger renewal") from ex
        raise ConfigEntryNotReady from ex

    hass.data[DOMAIN][config_entry.entry_id] = {
        "ticktick_auth": session.token
    }

    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)


async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Migrate old entry."""
    data = {**config_entry.data}
    return True
