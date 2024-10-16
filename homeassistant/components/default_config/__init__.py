"""Component providing default configuration for new users."""

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

DOMAIN = "default_config"

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Initialize default configuration."""
    if sys.platform.startswith(("linux", "win32", "darwin")):
        await async_setup_component(hass, "bluetooth", config)

    return True
