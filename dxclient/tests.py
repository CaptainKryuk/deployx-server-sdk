import unittest
import pytest
import random
from . import config
from . import __config
import logging
# from . import __config
"""
Tests:

Инициализация
    1. Создан ли дефолтный глобальный класс без sdk_key при инициализации? +
    2. Включены ли логи +
    3. Включен ли уровень логов INFO -

Установка конфига как класса Config()
    1. С валидным ключом
    2. С нулевым ключом
    3. С другим типом ключа

Установка конфига как словарь
    1. С валидным ключом
    2. С нулевым ключом
    3. С другим типом ключа

Установка просто ключа
    1. С валидным ключом
    2. С нулевым ключом
    3. С другим типом ключа


"""

# @pytest.fixture(scope='module')
# def config_data():
#     keys_list = ['sldgjlsfkj']
#     return config.Config(sdk_key=random.choice(keys_list))

# def test_config(config_data):
#     assert isinstance(config_data, config.Config) == True
#     # assert bad_config_data == 42

# @pytest.fixture(scope='class')
# def class_scope():
#     return (1, 3)


# @pytest.mark.usefixtures('class_scope')
# def test_func_1(class_scope):
#     assert class_scope == (1, 3)


# @pytest.mark.usefixtures('class_scope')
# class TestInitializationClass:

#     def test_1(self):
#         assert 1==1
    
#     def test_2(self, class_scope):
#         assert class_scope == (1, 3)


# ==============================================================
_config = __config


class TestDxclientInitialization:

    def test_is_global_config_created(self):
        global _config
        assert isinstance(_config, config.Config) == True
        assert _config.sdk_key == None

    def test_logging_is_working(self):
        if logging.getLogger():
            assert True
        else:
            assert False
    
