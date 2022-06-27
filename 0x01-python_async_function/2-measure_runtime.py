#!/usr/bin/env python3
"""
Measure the runtime
"""

import asyncio
import random
import time
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delays: int) -> float:
    """
    measures the total execution time for
     wait_n(n, max_delay), and returns total_time / n
    :param n:
    :param max_delays:
    :return:
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delays))
    elapsed = perf_counter() - start
    return elapsed
