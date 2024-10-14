#!/usr/bin/env python3
"""asynchronous coroutine taking  in an integer argument
with a default value of 10"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Delay"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
