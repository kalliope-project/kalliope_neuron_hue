# hue. Under construction. DO NOT INSTALL IT

## Synopsis

This neuron allow you to control your [Philips HUE](http://www2.meethue.com/en-us/about-hue/) lights from Kalliope.

## Installation

Install the neuron into your resource directory
```bash
kalliope install --git-url https://github.com/kalliope-project/kalliope_neuron_hue.git
```

Before being able to use the neuron, you must establish an initial connection with your bridge in order to allow Kalliope to interact with it.
To do that, run the python script and follow instructions
```bash
cd /path/to/your/resource_dir/neurons/hue
python bind_hue_bridge.py
```

## Options

The control will be based on group or light's names. You must set `groups_name` or `lights_name` or both parameter.

| parameter   | required | default | choices | comment                                                |
|-------------|----------|---------|---------|--------------------------------------------------------|
| bridge_ip   | YES      |         |         | The IP address of your HUE bridge                      |
| groups_name | NO       |         |         | List of group's name to switch                         |
| lights_name | NO       |         |         | List of light's name to switch                         |
| state       | YES      |         | on, off | Desired state of lights. Can be "on" or "off"          |
| brightness  | NO       |         | 0-100   | Percentage of brightness of lamps in the target group. |

## Return Values

This neuron does not return any value

## Synapses example

Here we switch on all lights on in the group called "bedroom"
```yml
 - name: "switch-on-bedroom"
   signals:
     - order: "turn the light on in the bedroom"
   neurons:
     - hue:
        bridge_ip: "192.168.0.7"
        groups_name:
         - "bedroom"
        state: "on"
```

Here we switch off all lights in the group called "hall" and "living-room"
```yml
 - name: "switch-on-bedroom"
   signals:
     - order: "turn the light on in the bedroom"
   neurons:
     - hue:
        bridge_ip: "192.168.0.7"
        groups_name:
         - "hall"
         - "living-room"
        state: "off"
```

Here we switch on a list of lights and set their brightness to the maximum level
```yml
 - name: "switch-on-bedroom"
   signals:
     - order: "turn the light on in the bedroom"
   neurons:
     - hue:
        bridge_ip: "192.168.0.7"
        lights_name:
         - "lamp1"
         - "lamp2"
        state: "on"
        brighness: 100
```

## Notes

> **Note:** Your Kalliope installation must be placed on a device which it's in the same network as the HUE bridge.

> **Note:** The binding between the bridge and Kalliope is based on the IP address. It means that the device that host Kalliope should not changes its IP address.
Consider the usage of a static IP or a DHCP reservation to be sure you will never change the IP address.

## Licence

MIT
