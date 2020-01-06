import requests

__env_key = None

api_url = "http://127.0.0.1:8000/api/client/v1/"

def set_key(key):
    """
    * install default enviroment key
    """

    global __env_key

    __env_key = key


def get_point(point_name, default):
    """
    Point_name using to get general point
    default using if request from api get False
    """

    global __env_key

    if __env_key is not None:

        response = requests.get(api_url + 'get_point/' + get_valid_env_key() + "/" + get_valid_point_name(point_name))
        
        if response.status_code == 200:
            return response.json()

        if response.status_code == 400:
            raise Exception(response.json())
        
    raise Exception("You must 'set_key' before getting point")


def get_valid_env_key():
    """
    check valid enviroment key
    """
    global __env_key 

    if (len(__env_key) == 64):
        return str(__env_key)

    raise Exception("Key must be hash64 and str type. Copy your key in DeployX dashboard.")


def get_valid_point_name(name):
    """
    check valid point name and replace " " with "--"
    need to send valid param in http request
    """
    if isinstance(name, str):
        return name.replace(" ", "--") 
    raise Exception("Name of point must be str.")


