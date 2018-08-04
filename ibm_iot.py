import sys
import time
import json
import paho.mqtt.client as mqtt

# import ibmiotf.device

host = 'oqpqg5.messaging.internetofthings.ibmcloud.com'
client_id = 'd:oqpqg5:temp_sensor_01:ts_02'
username = 'use-token-auth'
password = 'gdfKl!FZTaX9!!_Esm'
topic = 'iot-2/evt/temperature/fmt/json'



client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)
i = 0
while i<5:
  client.publish(topic, json.dumps({'t':40, 'h':45}))
  print('message published')
  time.sleep(5)
  i += 1
client.loop()
client.disconnect()
