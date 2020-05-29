import requests
import time

def make_request():
    general_list = []
    while True:
        url = yield general_list
        response = requests.get(url)
        general_list.append(response.status_code)

start = time.time()
pool = make_request()
next(pool)
for i in range(10):
    pool.send('https://ajax.googleapis.com')

pool.close()
end = time.time()
print(end - start)
