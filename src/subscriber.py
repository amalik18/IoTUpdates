import time

from mqtt_client import MQTTClient
import secrets


def main():
    PUBLISH = False
    def publish_update():
        """Method to handle the publishing of a download signal"""
        test_client.loop_start()
        test_client.publish(topic="download", message="True")
        time.sleep(5)

    def on_connect(client, userdata, flags, rc):
        """Connection callback"""
        if rc == 0:
            print(f"Successfully connected to MQTT Broker")
        else:
            print("Connection FAILED")

    def on_message(client, userdata, message):
        """Message received callback"""
        test_client.loop_stop()
        time.sleep(5)
        print(
            f"Message Received: {message.payload}\nTopic: {message.topic}\nQoS: {message.qos}\nRetain: {message.retain}")
        if float(message.payload.decode('utf-8').split(' ')[-1]) < 1.34:
            publish_update()

    test_client = MQTTClient(client_id=f'python-mqtt-{secrets.SystemRandom().randint(0, 1000)}',
                             broker='35.165.251.136',
                             transport="tcp",
                             port=1883)
    test_client.connect(connect_callback=on_connect, message_callback=on_message)

    test_client.subscribe(topic="package_version_new", qos=1)
    test_client.loop_start()
    time.sleep(5)



if __name__ == '__main__':
    main()
