import random
import subprocess
import time

from mqtt_client import MQTTClient


def main():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Successfully connected to MQTT Broker")
        else:
            print("Connection FAILED")

    def on_publish(client, userdata, mid):
        if mid:
            print(f"Message was published successfully")
        else:
            print(f"Errors occurred in publishing the message")

    test_client = MQTTClient(client_id=f'python-mqtt-{random.randint(0, 1000)}',
                             broker='35.165.251.136',
                             transport="websockets",
                             port=8033)
    test_client.connect(connect_callback=on_connect, publish_callback=on_publish)
    test_client.publish(topic="test",
                        message=get_data())

    test_client.loop_start()
    time.sleep(5)


def get_data():
    package_version = subprocess.Popen(['tar', '--version'], stdout=subprocess.PIPE)
    version_message = package_version.communicate()[0].decode('utf-8').split('\n')[0].split(' ')[-1]
    print(version_message)
    return f'The version of tar is: {version_message}'


if __name__ == '__main__':
    main()
