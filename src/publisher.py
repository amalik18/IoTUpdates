import subprocess
import time
import requests

from mqtt_client import MQTTClient
import secrets


def download_package():
    request_path = '35.165.251.136/packages/tar-1.34.tar.gz'
    output_path = 'tar-1.34.tar.gz'
    response = requests.get(request_path, stream=True)
    if response.status_code == 200:
        with open(output_path, 'wb') as output_file:
            output_file.write(response.raw.read())

def main():
    def on_connect(client, userdata, flags, rc):
        """Connection callback"""
        if rc == 0:
            print(f"Successfully connected to MQTT Broker")
        else:
            print("Connection FAILED")

    def on_publish(client, userdata, mid):
        """Successful publish callback"""
        if mid:
            print(f"Message was published successfully")
        else:
            print(f"Errors occurred in publishing the message")

    def on_message(client, userdata, message):
        """Subscription message received callback"""
        print(
            f"Message Received: {message.payload}\nTopic: {message.topic}\nQoS: {message.qos}\nRetain: {message.retain}")
        if message.payload.decode('utf-8') == "True":
            download_package()

    test_client = MQTTClient(client_id=f'python-mqtt-{secrets.SystemRandom().randint(0, 1000)}',
                             broker='35.165.251.136',
                             transport="tcp",
                             port=1883)
    test_client.connect(connect_callback=on_connect, publish_callback=on_publish, message_callback=on_message)
    test_client.publish(topic="package_version_new",
                        message=get_data())

    test_client.loop_start()
    time.sleep(5)
    test_client.loop_stop()
    time.sleep(5)
    test_client.subscribe(topic='download', qos=1)
    test_client.loop_forever()



def get_data():
    package_version = subprocess.Popen(['tar', '--version'], stdout=subprocess.PIPE)
    version_message = package_version.communicate()[0].decode('utf-8').split('\n')[0].split(' ')[-1]
    print(version_message)
    return f'The version of tar is: {version_message}'


if __name__ == '__main__':
    main()
