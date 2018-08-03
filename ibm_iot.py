

import ibmiotf.device

orgId = 'kfiraw'
deviceType = 'plc'
deviceId = 'plc_01'
authMethod = 'token'
authToken = 'iot7791ioT'


try:
  options = {
    "org": orgId,
    "type": deviceType,
    "id": deviceId,
    "auth-method": authMethod,
    "auth-token": authToken,
    "clean-session": True
  }
  client = ibmiotf.device.Client(options)
except ibmiotf.ConnectionException as e:
  print(e)