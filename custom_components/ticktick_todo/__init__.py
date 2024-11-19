import json
import logging
import os
from datetime import timedelta
from http import HTTPStatus
from pathlib import Path

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from aiohttp import ClientResponseError
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (CONF_NAME, CONF_FORCE_UPDATE, CONF_HOST, Platform, CONF_DOMAIN,
                                 CONF_ACCESS_TOKEN)
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from homeassistant.helpers import config_entry_oauth2_flow
from homeassistant.helpers.typing import ConfigType
from voluptuous import ALLOW_EXTRA

from custom_components.ticktick_todo.coordinator import TicktickUpdateCoordinator
from custom_components.ticktick_todo.pyticktick import openapi_client

_LOGGER = logging.getLogger(__name__)
_LOGGER.info('Starting tictick_todo')

MANIFEST = json.load(open("%s/manifest.json" % os.path.dirname(os.path.realpath(__file__))))
VERSION = MANIFEST["version"]
DOMAIN = MANIFEST[CONF_DOMAIN]
DEFAULT_NAME = MANIFEST[CONF_NAME]
PLATFORMS = [Platform.TODO]
ISSUE_URL = "https://github.com/konikvranik/hacs_ticktick/issues"
SCAN_INTERVAL = timedelta(seconds=20)

DEBUG = False

SCHEMA = {
    vol.Required(CONF_HOST): cv.string,
    vol.Required(CONF_ACCESS_TOKEN): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_FORCE_UPDATE, default=True): cv.boolean,
}

CONFIG_SCHEMA = vol.Schema({vol.Optional(DOMAIN): vol.Schema(SCHEMA)}, extra=ALLOW_EXTRA)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Netatmo component."""
    return True


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up ESPHome binary sensors based on a config entry."""

    coordinator_ = TicktickUpdateCoordinator(hass, config_entry, await _get_valid_token(config_entry, hass))
    config_entry.runtime_data = {'coordinator': coordinator_}
    #hass.data.setdefault(DOMAIN, {})[config_entry.entry_id] = coordinator
    await coordinator_.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)


async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Migrate old entry."""
    data = {**config_entry.data}
    return True


async def _get_valid_token(config_entry, hass):
    # Set unique id if non was set (migration)
    if not config_entry.unique_id:
        hass.config_entries.async_update_entry(config_entry, unique_id=DOMAIN)

    if DEBUG:
        return open(f'{Path.home()}/.ticktick_token').read().strip()
    implementation = await config_entry_oauth2_flow.async_get_config_entry_implementation(hass, config_entry)
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
    return session.token["access_token"]
