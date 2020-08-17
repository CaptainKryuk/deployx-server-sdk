from dxclient import src as dxclient
import datetime

# dxclient.set_sdk_key('3e2269e0666dfb82ff059438586f585e21c6b158d55c17c0a3fc7f5dbc74e018')

user = {
    'UNIQUE_IDENTIFIER': 'TEST'
}

dxclient.set_sdk_key("6ee4189e763c2742465eaa90294f6e3f19b2f91258d084f88905c3135486e6c8")

feature = dxclient.get('test', user, False)

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
