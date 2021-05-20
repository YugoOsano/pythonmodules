#!/usr/bin/python3.7
# transcribed from Python Jissen Nyumon p-256

import asyncio
import random

async def coroutine():
    return 1

async def call_web_api(url):
    print(f'send a request: {url}')
    # a random number in [0,1)
    await asyncio.sleep(random.random())
    print(f'got a response: {url}')
    return url

async def async_download(url):
    response = await call_web_api(url)
    return response

async def main():
    task = asyncio.gather(
        async_download('https://abc.com/'),
        async_download('https://def.com/'),
        async_download('https://ghi.com/'),
    )
    return await task

result = asyncio.run(coroutine())
print(result)

result = asyncio.run(main())
print(result)
