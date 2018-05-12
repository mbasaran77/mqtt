
import paho.mqtt.client as mqtt
import time

# broker = "test.mosquitto.org#
# broker = "test.mosquitto.org#
# broker = "test.mosquitto.org#

broker = "192.169.1.206"

client = mqtt.Client("python1")

print("connectting to broker ", broker)

client.connect(broker)

time.sleep(4)

client.disconnect()

