import aiohttp
import asyncio
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return response.status

async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(100):
            status = await fetch(session, 'https://ajax.googleapis.com')

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    end = time.time()
    print(end-start)