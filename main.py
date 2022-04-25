from paho.mqtt import client as mqtt_client


def publish():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Successfully connected to MQTT Broker")
        else:
            print("Connection FAILED")

    test_client = mqtt_client.Client(client_id="test_client",
                                     clean_session=True,
                                     )
    test_client.on_connect = on_connect
    test_client.connect(host='35.165.251.136',
                        port=1883)

    test_client.loop_start()
    test_client.publish(topic="test",
                        payload="Hello this is a test",
                        qos=1,
                        retain=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    publish()
