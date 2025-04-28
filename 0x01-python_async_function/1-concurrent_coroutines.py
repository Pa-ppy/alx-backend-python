#!/usr/bin/env python3
"""Module that spawns multiple coroutines and
returns delays in ascending order."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return list of
    delays in ascending order."""
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    results = []
    for task in asyncio.as_completed(delays):
        result = await task
        results.append(result)
    return results
