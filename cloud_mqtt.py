
import paho.mqtt.client as mqtt
import os
from urllib.parse import urlparse
import time
# Define event callbacks


def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))


def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')
url = urlparse(url_str)
topic = url.path[1:] or 'vp_1'

# Connect
mqttc.username_pw_set("vkrvmcxx", "FwXk5dCG2gX2")
mqttc.connect('m21.cloudmqtt.com', 15253)

# Start subscribe, with QoS level 0
mqttc.loop()
i = 0
temp_0 = 15
while i<5:
    if temp_0 >= 45:
        temp_0 = 15
    mqttc.subscribe("house/temp_0", 0)
    # Publish a message
    mqttc.publish("house/temp_0", temp_0)
    time.sleep(4)
    i += 1
    temp_0 = temp_0 + 5
# Continue the network loop, exit when an error occurs
# rc = 0
# while rc == 0:
#     rc = mqttc.loop()
#     time.sleep(5)
#     if temp_0 >= 40:
#         temp_0 = 15
#     temp_0 = temp_0 + 5
#
# print("rc: " + str(rc))