#!/usr/bin/env python3
"""Module that measures runtime of running async_comprehension 4 times."""

import asyncio
import time


async def measure_runtime() -> float:
    """Measure total runtime of 4 async_comprehension calls run in parallel."""
    async_comprehension = (
        __import__('1-async_comprehension').async_comprehension
    )
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
