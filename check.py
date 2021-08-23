from package.src import dxclient


dxclient.set_sdk_key("c5d5ee91c434e3f80085733aae94211626ad839162e9f8cb37f74b91007f51e5")

point = dxclient.get("test", {'unique_identifier': 'fff', 'username': 'bo'})

print(type(point))

if point:
  print("работает новая версия")
else:
  print("работает старая версия")