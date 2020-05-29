import dxclient
import ldclient
from dxclient import config
import datetime

dxclient.set_sdk_key('3169aa5d3802aeb0bc444f5cbf08336ea59b08f372af086f91e59d7dbf2f6e62')

user = {
    'unique_identifier': 'MYIDENTIFIER228',
    'username': 'captainkryuk',
    'first_name': 'andrey',
    'email': 'bestrongwb@gmail.com',
    'last_name': 'kryukov'  
}

feature = dxclient.get('point', user, False)

if feature:
    print('work')
else:
    print('not work')


# import ldclient

# if __name__ == "__main__":
#   ldclient.set_sdk_key("sdk-832f0015-db2b-4882-ba1e-84dd32b75723")


# user = {
#   "key": "VASIC228",
#   "firstName": "Vasil",
#   "lastName": "kit",
#   "custom": {
#     "groups": "beta_testers"
#   }
# }

# show_feature = ldclient.get().variation("second-point", user, False)
# show_feature = ldclient.get().variation("new-point", user, False)

# if show_feature:
#   print("Showing your feature")
# else:
#   print("Not showing your feature")

# ldclient.get().close()