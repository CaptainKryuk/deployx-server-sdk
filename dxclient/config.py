import logging

class Config:

    def __init__(self, 
                 sdk_key=None,
                 offline=False,
                 api_url='127.0.0.1'):
        self.sdk_key = sdk_key
        self.offline = offline
        self.api_url = api_url
    @classmethod
    def default(cls):
        return cls

    def set_config(self, config):
        if isinstance(config, Config):
            return self._set_instance_config(config)

        if isinstance(config, dict):
            return self._set_dict_config(config)

        raise AttributeError('Config must be a dictionary or a Config() type. Example of dict attributes: { UNIQUE_IDENTIFIER: "some hash", username: "Josh Bold" }.\n'
                             ' Config() instance you can import from dxclient.config.')
    
    def _set_instance_config(self, config):
        logging.info('Install config via Config() instance.')
        if config.sdk_key:
            return config
        raise AttributeError('Config intance must include sdk_key attr.')

    def _set_dict_config(self, config):
        logging.info('Install config with config dictionary.')
        for key in config:
            if hasattr(self, key) and isinstance(config[key], str):
                setattr(self, key, config[key])
        return self

        
    def set_sdk_key(self, key):
        if isinstance(key, str):
            self.sdk_key = key
            return
        raise AttributeError('SDK_KEY must be str() type.')