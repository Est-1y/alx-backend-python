#!/usr/bin/env python3
"""asynchronous coroutine taking  in an integer argument
with a default value of 10"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
