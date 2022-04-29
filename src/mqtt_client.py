import random
import time

from paho.mqtt import client as mqtt_client
from paho.mqtt.client import MQTTv31, MQTT_ERR_SUCCESS, MQTT_ERR_NO_CONN, MQTT_ERR_QUEUE_SIZE, MQTTv5


class MQTTClient:
    """Wrapper around the MQTT Client provided by Paho-MQTT"""
    def __init__(self, client_id, broker, port=1883, transport="tcp", protocol=MQTTv31):
        """Client initialization. Similar parameters provided to the Paho-MQTT Client

        Args:
            client_id (string): String to describe the MQTT Client
            broker (string): IP Address or FQDN of the server running the MQTT Broker
            port (int, optional): Which port for the client to utilize.. Defaults to 1883.
            transport (str, optional): transport method to use (tcp or websockets). Defaults to "tcp".
            protocol (_type_, optional): MQTT protocol version to use. Defaults to MQTTv31.
        """
        self.client_id = client_id
        self.transport = transport
        self.protocol = protocol
        self.port = port
        self.broker = broker
        self.paho_client = mqtt_client.Client(client_id=client_id, transport=transport, protocol=protocol)

    def connect(self, connect_callback=None, publish_callback=None, subscribe_callback=None, message_callback=None):
        """Method to establish a connection between the Client and Broker.

        Args:
            connect_callback (function, optional): Function that gets invoked when a connection is successful. Defaults to None.
            publish_callback (function, optional): Function that gets invoked when a publish request is successfully sent. Defaults to None.
            subscribe_callback (function, optional): Function that gets invoked when subscription is successful. Defaults to None.
            message_callback (function, optional): Function that gets invoked whenever a message is received to a subscribed topic. Defaults to None.

        Returns:
            _type_: returns an instance of the Paho-MQTT Client
        """
        self.paho_client.on_connect = connect_callback
        self.paho_client.on_publish = publish_callback
        self.paho_client.on_subscribe = subscribe_callback
        self.paho_client.on_message = message_callback
        self.paho_client.connect(host=self.broker, port=self.port)
        return self.paho_client

    def publish(self, topic, message):
        """Wrapper around the publish() method from Paho-MQTT.Client.publish()

        Args:
            topic (str): topic to which the message will be published
            message (str): the message to publish, the payload.
        """
        result = self.paho_client.publish(topic=topic, payload=message, qos=1, retain=False)
        result_status = result[0]
        if result_status == MQTT_ERR_SUCCESS:
            print(f"Publish Message: {message}, SUCCESS")
        elif result_status == MQTT_ERR_NO_CONN:
            print(f"Publish Message: {message}, FAILED\nPlease make sure the client is connected first.")
        elif result_status == MQTT_ERR_QUEUE_SIZE:
            print(f"The message was not sent nor queued. You have reached the max_queued_messages_set limit.")

    def subscribe(self, topic, qos=0):
        """_summary_

        Args:
            topic (str): Topic which will be monitored.
            qos (int, optional): QoS value. Defaults to 0.
        """
        result = self.paho_client.subscribe(topic=topic, qos=qos)
        result_status = result[0]
        if result_status == MQTT_ERR_SUCCESS:
            print(f"Subscribe to Topic: {topic}, SUCCESS")
        elif result_status == MQTT_ERR_NO_CONN:
            print(f"Subscribe to Topic: {topic}, FAILED\nPlease make sure the client is connected first.")

    def loop_start(self):
        """Wrapper around Paho-MQTT.client.loop_start()"""
        self.paho_client.loop_start()

    def loop_forever(self):
        """Wrapper around Paho-MQTT.client.loop_forever()"""
        self.paho_client.loop_forever()

    def loop_stop(self):
        """Wrapper around Paho-MQTT.client.loop_stop()"""
        self.paho_client.loop_stop()

    def loop(self, duration):
        """Wrapper around the Paho-MQTT.client.loop() method

        Args:
            duration (int): length of duration in seconds
        """
        self.paho_client.loop(duration)
