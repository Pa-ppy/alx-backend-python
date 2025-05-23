#!/usr/bin/env python3
"""Module that spawns multiple task_wait_random and
returns delays in ascending order."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return
    list of delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
