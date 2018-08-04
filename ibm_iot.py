import sys
import time
import json
import paho.mqtt.client as mqtt

# import ibmiotf.device

host = 'oqpqg5.messaging.internetofthings.ibmcloud.com'
client_id = 'd:oqpqg5:Sensor:TempSensor_1'
username = 'use_token_auth'
password = 'token'
topic = 'iot-2/evt/temperature/fmt/json'



client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)

while True:
  client.publish(topic, json.dumps({'t':40, 'h':45}))
  print('message published')
  time.sleep(5)

client.loop()
client.disconnect()
