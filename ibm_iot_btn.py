import sys
import time
import json
import paho.mqtt.client as mqtt

# import ibmiotf.device

host = 'oqpqg5.messaging.internetofthings.ibmcloud.com'
client_id = 'd:oqpqg5:Buttons:Button'
username = 'use-token-auth'
password = 'H1qNC5-TzKt_8fFV*j'
topic = 'iot-2/evt/button/fmt/json'

client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
i = 0


while i < 5:
    payload = {"Button": "on"}
    client.publish(topic, json.dumps(payload))
    print('message published')
    time.sleep(5)
    i += 1
client.loop()
client.disconnect()
