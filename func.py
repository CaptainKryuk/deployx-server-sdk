from package.src import dxclient

dxclient.set_sdk_key("39f16f86de5419fd974eec6c6611526120cbf11a76c4a1f4fe2fb5c294989496")

flag = dxclient.get("test", {'unique_identifier': 'vic', 'username': 'Johny'}, True)

if flag:
  print("работает новая версия")
else:
  print("работает старая версия")