import sys
import time
import json
import paho.mqtt.client as mqtt

host = 'oqpqg5.messaging.internetofthings.ibmcloud.com'
client_id = 'd:oqpqg5:Bulbs:Bulb'
username = 'use-token-auth'
password = 'YsbjUOoOrXJx8*h&ek'
topic = 'iot-2/cmd/state/fmt/json'


def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))


def on_message(client, obj, msg):
    button = json.load(msg.payload)["state"]
    if button == "on":
        print("btn on")
    else:
        print("btn off")

    # print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print(button)


def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, obj, level, string):
    print(string)


client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
client.subscribe(topic)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
client.disconnect()
