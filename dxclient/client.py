import logging
from urllib3 import HTTPConnectionPool, HTTPSConnectionPool
from .store import FeaturePointStore
import json

class DXClient:

    def __init__(self, config):
        self.config = config

        logging.info('Start Pool connection to host.')
        self.pool = HTTPConnectionPool('127.0.0.1', port=8000)
        # print(self.pool2.num_connections, self.pool.num_connections)

    def get_point(self, point_key, user, default=None):
        r = self.pool.request('PUT', 
                              '/api/client/v1/get_point/{}/{}/'.format(self.config.sdk_key, point_key),
                              headers={'Content-Type': 'application/json'},
                              body=json.dumps(user))
        logging.info("{} {}".format(r.status, r.data))
        if r.status == 200:
            self.store = FeaturePointStore()

        if r.status == 400:
            raise TypeError(r.data)
        elif r.status == 500:
            raise ConnectionError("Error when try to connect to server.")
            # TODO Добавить логику перевода клиента в статус offline


    def close(self):
        if self.pool.num_connections:
            self.pool.close()
        logging.info('Closing connection in initialized client instance.')
