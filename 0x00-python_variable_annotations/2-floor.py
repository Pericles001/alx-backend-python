#!/usr/bin/env python3
"""
Basic annotations - floor
"""


def floor(n: float) -> int:
    """
    takes a float and returns the floor of the float
    :param n:
    :return:
    """
    return int(n) if n > 0 else int(n) - 1
