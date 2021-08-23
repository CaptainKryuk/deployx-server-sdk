from . import *


#* Все ок

#* user пустой
#* identifier капсом
#* identifier = '' (пустой)
#* поля больше 255 символов

#* выключен redis
#* флаг не сохранен, нет подключения к сети
#* флаг сохранен, отключилась сеть
#* пользователь получил первый флаг и если запрашивает второй, то ничего не получает

# нет инета
# + 2 флага в системе выставлены false, default - True, client_debug = True. Результат - True на обоих так как первое значение берется из default
# + тоже самое, что сверху, только client_debug - False, и перед этим был запрос, который сохранил значения False в redis. Результат - оба False, так как сохраненные в редис значения False
# _ тоже самое, что на строчку выше, только редис база пустая и раньше запросов не было. Результат оба True, так как берутся из default
# тоже самое, что на строчку выше, только default Значения не передаются. Результат - AttributeError 

CONFIG = {
    'sdk_key': 'c5d5ee91c434e3f80085733aae94211626ad839162e9f8cb37f74b91007f51e5'
}

@pytest.mark.incremental
class TestNormalExperiment:

    def test_all_valid_data_and_flag_enabled(self):
        user = {
            'unique_identifier': 'MYIDENTIFIER123',
            'username': 'captainkryuk',
            'first_name': 'andrey',
            'email': 'bestrongwb@gmail.com',
            'last_name': 'kryukov'  
        }
        dxclient.set_sdk_key(CONFIG['sdk_key'])
        feature = dxclient.get('test', user, False)
        assert feature == True


    def test_caps_user_and_flag_disabled(self):
        user = {
            'UNIQUE_IDENTIFIER': 'TEST'
        }
        dxclient.set_sdk_key(CONFIG['sdk_key'])
        feature = dxclient.get('test', user, False)
        assert feature == True

    def test_caps_user_and_flag_2disabled(self):
        user = {
            'UNIQUE_IDENTIFIER': 'TEST'
        }
        dxclient.set_sdk_key(CONFIG['sdk_key'])
        feature = dxclient.get('test', user, False)
        assert feature == True


    def test_blank_dict_user_and_flag_enabled(self):
        """ 
        * should create user with unique_identifier == '-' 
        * if user already created just get flag from redis
        """
        user = {}
        dxclient.set_sdk_key(CONFIG['sdk_key'])
        feature = dxclient.get('test', user, False)
        assert feature == True


    def test_blank_identifier_user_and_flag_enabled(self):
        """ 
        * should create user with unique_identifier == '-' 
        * if user already created just get flag from redis
        """
        user = {
            'UNIQUE_IDENTIFIER': ''
        }
        dxclient.set_sdk_key(CONFIG['sdk_key'])
        feature = dxclient.get('test', user, False)
        assert feature == True


    def test_all_blank_user_and_flag_enabled(self):
        user = {
            'unique_identifier': '',
            'username': '',
            'first_name': '',
            'email': '',
            'last_name': ''          
        }
        dxclient.set_sdk_key(CONFIG['sdk_key'])
        feature = dxclient.get('test', user, False)
        assert feature == True


    def test_blank_identifire_fill_user_and_flag_enabled(self):
        user = {
            'unique_identifier': '',
            'username': 'username',
            'first_name': 'andrey',
            'email': 'bestrongwb@gmail.com',
            'last_name': 'kryukov'          
        }
        dxclient.set_sdk_key(CONFIG['sdk_key'])
        feature = dxclient.get('test', user, False)
        assert feature == True
