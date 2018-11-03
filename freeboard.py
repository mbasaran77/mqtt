import sys
import time
import json
import paho.mqtt.client as mqtt

host = 'quickstart.messaging.internetofthings.ibmcloud.com'
client_id = 'dev_1'
username = 'quickstart'
password = 'ascs1234'
topic = 'iot-2/type/+/id/DEVICEID/evt/+/fmt/json'


def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))


def on_message(client, obj, msg):
    print(msg.payload)
    button = json.loads(msg.payload)["state"]
    # button = msg.payload[1]
    print(button)
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
