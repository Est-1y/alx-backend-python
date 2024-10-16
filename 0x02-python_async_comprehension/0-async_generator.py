#!/usr/bin/env python3
"""Async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generating 10 number sequence
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
