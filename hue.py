import ipaddress
import logging
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException, InvalidParameterException


# TODO: install.yml: ipaddress + phue
from phue import Bridge

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Hue(NeuronModule):
    def __init__(self, **kwargs):
        super(Hue, self).__init__(**kwargs)

        self.bridge_ip = kwargs.get('bridge_ip', None)
        self.group_name = kwargs.get('group_name', None)
        self.light_name = kwargs.get('light_name', None)
        self.state = kwargs.get('state', None)
        self.brightness = kwargs.get('brightness', None)

        # check if parameters have been provided
        if self._is_parameters_ok():
            # connect to the bridge
            self.b = Bridge(self.bridge_ip)
            # TODO switch to a list of group instead of unique group name
            if self.group_name is not None:
                # get all groups
                groups = self.b.get_group()
                # get the group id from the name
                lights_ids = self._get_lights_id_by_from_group_name(groups, self.group_name)
                # switch status of each light in the group depending on the state
                logger.debug("Lights id: %s" % lights_ids)
                if lights_ids is not None:
                    for light_id in lights_ids:
                        self.switch_light(int(light_id))

            # TODO switch to a list of light name instead of unique name
            if self.light_name is not None:
                # get the id of the target light by its name
                light = self.b.get_light(self.light_name)
                if light is not None:
                    self.switch_light(self.light_name)

    def _is_parameters_ok(self):
        # test bridge ip is set
        if self.bridge_ip is None:
            raise MissingParameterException("Hue neuron needs a bridge_ip")

        # test if the ip is a valid ip. The following line will raise an exception
        bridge_ip_unicode = self.bridge_ip.decode('utf-8')
        ipaddress.ip_address(bridge_ip_unicode)

        # user must set a group name of a light name
        if self.group_name is None and self.light_name is None:
            raise MissingParameterException("Hue neuron needs at least a group name or a light name")

        # user cannot use both group name and light name
        if self.group_name is not None and self.light_name is not None:
            raise InvalidParameterException(
                "Hue neuron cannot be used with both group_name and light_name")

        # test state ok
        if self.state is None:
            raise MissingParameterException("Hue neuron needs a state \"on\" or \"off\"")
        if self.state not in ["on", "off"]:
            raise InvalidParameterException("Hue: state must be \"on\" or \"off\"")

        if self.brightness is not None:
            r = range(0, 101)
            if int(self.brightness) not in r:
                raise InvalidParameterException("Hue: brightness must be in range 0:100")

        return True

    @staticmethod
    def _get_lights_id_by_from_group_name(groups, group_name_to_find):
        """
        Return a list of light ID of the group by its name
        :param groups: list of group from the bridge api
        :param group_name_to_find: string group to find in the list
        :return: list of lights IDs
        """
        lights_id = None
        for group in groups:
            group_id = str(group)
            group_dict = groups[group_id]
            if group_dict["name"] == group_name_to_find:
                lights_id = group_dict["lights"]
                break
        return lights_id

    @staticmethod
    def _get_boolean_from_state(state):
        if state == "on":
            return True
        return False

    def switch_light(self, light_identifier):
        """
        Call the HUE api to switch the light depending on the desired state
        :param light_identifier: ID or name of the light
        """
        logger.debug("HUE: Switching light %s to state %s" % (light_identifier, self.state))
        self.b.set_light(light_identifier, 'on', self._get_boolean_from_state(self.state))
