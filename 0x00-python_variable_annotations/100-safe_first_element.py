#!/usr/bin/env python3
"""Module that safely returns the first element of a sequence, or None."""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence
    or None if the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
