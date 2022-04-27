import time

from mqtt_client import MQTTClient
import random


def main():
    PUBLISH = False

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Successfully connected to MQTT Broker")
        else:
            print("Connection FAILED")

    def on_message(client, userdata, message):
        test_client.loop_stop()
        print(
            f"Message Received: {message.payload}\nTopic: {message.topic}\nQoS: {message.qos}\nRetain: {message.retain}")
        if int(message.payload.split(' ')[-1]) < 1.34:
            PUBLISH = True

    test_client = MQTTClient(client_id=f'python-mqtt-{random.randint(0, 1000)}',
                             broker='35.165.251.136',
                             transport="websockets",
                             port=8033)
    test_client.connect(connect_callback=on_connect, message_callback=on_message)

    test_client.subscribe(topic="package_version", qos=1)
    test_client.loop_forever()

    if PUBLISH:
        test_client.loop_start()
        test_client.publish(topic="download", message="True")
        time.sleep(5)


if __name__ == '__main__':
    main()
