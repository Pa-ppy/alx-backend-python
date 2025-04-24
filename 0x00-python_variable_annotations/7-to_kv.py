#!/usr/bin/env python3
"""Module that provides a function to return a tuple from a
string and a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the first element is a string and the
    second is the square of the number."""
    return (k, float(v ** 2))
