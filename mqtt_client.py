
import paho.mqtt.client as mqtt
import time


def on_log(client, userdata, level, buf):
    print("log ", buf)


def on_connect(client, userdata,flags, rc):
    if rc == 0:
        print("connected ok")
    else:
        print("bad connection returned code = ", rc)


def on_disconnect(client, userdata,flags, rc = 0):
    print("disconnected result code = ", rc)


def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8"))
    print("mesage received", m_decode)


broker = "192.168.1.206"
client = mqtt.Client("python1")     # create new instance

client.on_connect = on_connect  # bind call back function call
client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_message = on_message

print("connectting to broker ", broker)

# client.connect("iot.eclipse.org", 1883, 60)  # connect to broker

client.connect("test.mosquitto.org", 1883, 60)  # connect to broker

client.loop_start()
client.subscribe("house/temp_0")
client.publish("house/temp_0", 12.0)
time.sleep(4)

client.disconnect()     # disconnect
client.loop_stop()
