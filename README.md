# py-mqtt-tools

The python scripts use [Eclipse Paho](https://pypi.org/project/paho-mqtt/) as MQTT client and [termcolor](https://pypi.org/project/termcolor/) for having a colorized output in the console. The dependencies can be installed with:

```bash
pip3 install paho-mqtt
pip3 install termcolor
```

This repository contains the following Python applications:

- MQTT publisher (`clients/publisher.py`)
- MQTT subscriber (`clients/subscriber.py`)

## Mosquitto broker setup (macOS)

The MQTT broker [mosquitto](https://mosquitto.org/) can be installed on MacOS with:

```bash
brew install mosquitto
```

The broker can be run with:

```bash
/usr/local/opt/mosquitto/sbin/mosquitto -c ./mosquitto.conf
```

where `./mosquitto.conf` is a simple configuration file contained in this repo.

The broker will listen on default port 1883 and accept all connections. No username and passwords are required. To stop the broker simply press CMD-C.