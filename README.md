# hue. Under construction. DO NOT INSTALL IT

## Synopsis

This neuron allow you to control your [Philips HUE](http://www2.meethue.com/en-us/about-hue/) lights from Kalliope.

## Installation

Install the neuron into your resource directory
```bash
kalliope install --git-url https://github.com/kalliope-project/kalliope_neuron_hue.git
```

Before being able to use the neuron, you must establish an initial connection with your bridge.
To do that, run the python script and follow instruction
```bash
cd /path/to/your/resource_dir/neurons/hue
python bind_hue_bridge.py
```

## Options

The control will be based on group or light names.


## Return Values

Only necessary when the neuron use a template to say something

| name      | description                        | type       | sample                    |
|-----------|------------------------------------|------------|---------------------------|
| value_key | dictionary containing all the data | dictionary | {"name":"me", "email": 2} |
| value_key | list of value                      | list       | ["val1", "val2", "val3"]  |
| value_key | string value                       | string     | "2"                       |


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
         - "hall"
        state: "on"
```

Here we switch off all lights in the group called "bedroom" and "living-room"
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

## Templates example

Description of the template
```
This is a var {{ var }}
{% for item in items %}
 This is the  {{ item }}
{% endfor %}
```

## Notes

> **Note:** Your Kalliope installation must be placed on a device which it's in the same network as the HUE bridge.

> **Note:** The binding between the bridge and Kalliope is based on the IP address. It means that the device that host Kalliope should not changes its IP address.
Consider the usage of a static IP or a DHCP reservation to be sure you will never change the IP address.

## Licence

MIT
