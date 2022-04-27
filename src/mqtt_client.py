import random
import time

from paho.mqtt import client as mqtt_client
from paho.mqtt.client import MQTTv31, MQTT_ERR_SUCCESS, MQTT_ERR_NO_CONN, MQTT_ERR_QUEUE_SIZE, MQTTv5


class MQTTClient:
    def __init__(self, client_id, broker, port=1883, transport="tcp", protocol=MQTTv31):
        self.client_id = client_id
        self.transport = transport
        self.protocol = protocol
        self.port = port
        self.broker = broker
        self.paho_client = mqtt_client.Client(client_id=client_id, transport=transport, protocol=protocol)

    def connect(self, connect_callback=None, publish_callback=None, subscribe_callback=None, message_callback=None):
        self.paho_client.on_connect = connect_callback
        self.paho_client.on_publish = publish_callback
        self.paho_client.on_subscribe = subscribe_callback
        self.paho_client.on_message = message_callback
        self.paho_client.connect(host=self.broker, port=self.port)
        return self.paho_client

    def loop_start(self):
        self.paho_client.loop_start()

    def loop_forever(self):
        self.paho_client.loop_forever()

    def publish(self, topic, message):
        result = self.paho_client.publish(topic=topic, payload=message, qos=1, retain=False)
        result_status = result[0]
        if result_status == MQTT_ERR_SUCCESS:
            print(f"Publish Message: {message}, SUCCESS")
        elif result_status == MQTT_ERR_NO_CONN:
            print(f"Publish Message: {message}, FAILED\nPlease make sure the client is connected first.")
        elif result_status == MQTT_ERR_QUEUE_SIZE:
            print(f"The message was not sent nor queued. You have reached the max_queued_messages_set limit.")

    def subscribe(self, topic, qos=0):
        result = self.paho_client.subscribe(topic=topic, qos=qos)
        result_status = result[0]
        if result_status == MQTT_ERR_SUCCESS:
            print(f"Subscribe to Topic: {topic}, SUCCESS")
        elif result_status == MQTT_ERR_NO_CONN:
            print(f"Subscribe to Topic: {topic}, FAILED\nPlease make sure the client is connected first.")

    def loop_start(self):
        self.paho_client.loop_start()

    def loop_forever(self):
        self.paho_client.loop_forever()

    def loop_stop(self):
        self.paho_client.loop_stop()
