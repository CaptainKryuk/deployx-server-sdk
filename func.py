import dxclient

dxclient.set_sdk_key("35891ef8a8214c1e0a79ceef8b2e80230a41a40bc1162fea6d8bad37047bfc4a")

point = dxclient.get("api", {}, True)

if point:
  print("работает новая версия")
else:
  print("работает старая версия")