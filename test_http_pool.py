from urllib3 import HTTPConnectionPool
import time

__pool = None

def start_pool():
    global __pool
    __pool =  HTTPConnectionPool('ajax.googleapis.com', maxsize=10)


def make_request():

    __pool.request('GET', '/ajax/services/search/web', 
                   fields={'q': 'urllib3', 'v': '1.0'})

start = time.time()
start_pool()

for i in range(100):
    make_request()

print(__pool.num_connections, __pool.num_requests)
end = time.time()
print(end - start)