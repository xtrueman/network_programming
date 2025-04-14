#!/usr/bin/env python3

import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello, world!")

asyncio.run(say_hello())
