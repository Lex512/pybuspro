import logging

import voluptuous as vol

# Import the device class from the component that you want to support
from homeassistant.components.light import ATTR_BRIGHTNESS, Light, PLATFORM_SCHEMA, SUPPORT_BRIGHTNESS
from homeassistant.const import CONF_HOST, CONF_USERNAME, CONF_PASSWORD
import homeassistant.helpers.config_validation as cv

# Home Assistant depends on 3rd party packages for API specific code.
# REQUIREMENTS = ['awesome_lights==1.2.3']

_LOGGER = logging.getLogger(__name__)

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Optional(CONF_USERNAME, default='admin'): cv.string,
    vol.Optional(CONF_PASSWORD): cv.string,
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the Awesome Light platform."""
    # import awesomelights

    # Assign configuration variables. The configuration check takes care they are
    # present.
    host = config.get(CONF_HOST)
    username = config.get(CONF_USERNAME)
    password = config.get(CONF_PASSWORD)

    # Setup connection with devices/cloud
    # hub = awesomelights.Hub(host, username, password)
    _LOGGER.info("hub = awesomelights.Hub(host, username, password)")

    # Verify that passed in configuration works
    # if not hub.is_valid_login():
    #    _LOGGER.error("Could not connect to AwesomeLight hub")
    #    return

    # Add devices
    # add_devices(AwesomeLight(light) for light in hub.lights())
    add_devices([AwesomeLight(Light)])



class AwesomeLight(Light):
    """Representation of an Awesome Light."""

    def __init__(self, light):
        """Initialize an AwesomeLight."""
        #self._light = light
        self._name = "light.name"
        self._state = None
        self._brightness = None
        self._supported_features = SUPPORT_BRIGHTNESS

    @property
    def name(self):
        """Return the display name of this light."""
        return self._name

    @property
    def brightness(self):
        """Return the brightness of the light.

        This method is optional. Removing it indicates to Home Assistant
        that brightness is not supported for this light.
        """
        return self._brightness

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Instruct the light to turn on.

        You can skip the brightness part if your light does not support
        brightness control.
        """
        self._brightness = 100
        self._state = 'on'
        #self._light.brightness = kwargs.get(ATTR_BRIGHTNESS, 255)
        #self._light.turn_on()
        _LOGGER.info("turn_on() is called")

    def turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        #self._light.turn_off()
        self._brightness = 0
        self._state = 'off'
        _LOGGER.info("turn_off() is called")

    def update(self):
        """Fetch new state data for this light.

        This is the only method that should fetch new data for Home Assistant.
        """
        #self._light.update()
        #self._state = 'on' #self._light.is_on()
        #self._brightness = 80  #self._light.brightness
        _LOGGER.info("update() is called")
		
		