#!/usr/bin/env python3
"""
Complex types - function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns function that multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
