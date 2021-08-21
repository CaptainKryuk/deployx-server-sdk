from package.src import dxclient


dxclient.set_sdk_key("39f16f86de5419fd974eec6c6611526120cbf11a76c4a1f4fe2fb5c294989496")
dxclient.set_debug(False)

point = dxclient.get("test", {})

if point:
  print("работает новая версия")
else:
  print("работает старая версия")

point2 = dxclient.get('test2', {})
if point2:
  print('Во второй новая')
else:
  print("Во второй старая")