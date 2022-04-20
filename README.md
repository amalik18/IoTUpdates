# Goal
The goal of this project was to create an OTA mechanism which shows a proof of concept on how this could operate in
the real world.


# Setup

### Broker
For this demo an Ubuntu machine was used. Below are the steps to install the Mosquitto MQTT broker and the necessary
packages.

```bash
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto mosquitto_clients
sudo apt clean
```

To start the service: `sudo service mosquitto start`

To customize your Mosquitto broker please edit the file in `/etc/mosquitto/mosquitto.conf`

### Client
To setup the client all you need is Python. It should be vended by default with the Ubuntu distribution but in case it
isn't, follow the steps below:

```bash
sudo apt-get update
sudo apt-get install python3
```

Once you have Python up and running you will need the `paho-mqtt` library. This can be installed using `pip`

```bash
python3 -m pip install paho-mqtt
```

Once all of that is done, please pull down the files from this GitHub link: 



