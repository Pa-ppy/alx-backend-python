#!/usr/bin/env python3
"""Module that provides a function to sum a mixed list of ints and floats."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all integers and floats in a list as a float."""
    return sum(mxd_lst)
