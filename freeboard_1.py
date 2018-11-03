import sys
import time
import json
import paho.mqtt.client as mqtt

# import ibmiotf.device


host = 'quickstart.messaging.internetofthings.ibmcloud.com'
client_id = 'quickstart'
username = 'quickstart'
password = 'ascs1234'
topic = 'dev_1/evt/temperature/fmt/json'  # 'iot-2/type/+/id/dev_1/evt/+/fmt/json'

client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.connect(host, 8883, 60)
i = 0



while i < 5:
    client.publish(topic, json.dumps({'t': 40, 'h': 45}))
    print('message published')
    time.sleep(5)
    i += 1
client.loop()
client.disconnect()
