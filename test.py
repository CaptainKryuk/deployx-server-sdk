from dxclient import src as dxclient
import datetime

# dxclient.set_sdk_key('3e2269e0666dfb82ff059438586f585e21c6b158d55c17c0a3fc7f5dbc74e018')

user = {
    'UNIQUE_IDENTIFIER': 'osdjflsdmf',
    'username': 'userOK',
    'email': 'mybitch@mail.ru'
}

dxclient.set_sdk_key("636f20ddba3ef43eb7ddeea80386220f1ad91afbe72e34579532d789e53c5df9")

feature = dxclient.get('home', user, False)

if feature:
    print('work')
else:
    print('not work')


# ldclient.set_sdk_key("sdk-bd422093-1a6b-4a8c-a329-7f5b8c20d2e0")


# user = {
#   "key": "VASIC228",
#   "firstName": "Vasil",
#   "lastName": "kit",
#   "custom": {
#     "groups": "beta_testers"
#   }
# }

# show_feature = ldclient.get().variation("second-point", user, False)
# if show_feature:
#   print("Showing your feature")
# else:
#   print("Not showing your feature")

# ldclient.get().close()
