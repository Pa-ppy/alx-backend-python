#!/usr/bin/env python3
"""Module that collects random numbers using async comprehension."""

from typing import List


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using comprehension."""
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
