import ibmiotf.application
import time
import json


options = {
    "org": "oqpqg5",
    "id": "app1",
    "auth-method": "apikey",
    "auth-key": "a-oqpqg5-ffv6z5cmkm",
    "auth-token": "zs&HM&a&ZZwJ4c4v?",
    "clean-session": True
}

sourceDeviceType = "Buttons"
sourceDeviceId = "Button"
sourceEvent = "button"

targetDeviceType = "Bulbs"
targetDeviceId = "Bulb"


def ButtonCallback(event):
    print("got event" + json.dumps(event.data))
    button = event.data["Button"]
    commandData = {"state": button }
    client.publishCommand(targetDeviceType, targetDeviceId, "state", "json", commandData)


client = ibmiotf.application.Client(options)
client.connect()
client.deviceEventCallback = ButtonCallback
client.subscribeToDeviceEvents(deviceType=sourceDeviceType, deviceId=sourceDeviceId, event=sourceEvent)

