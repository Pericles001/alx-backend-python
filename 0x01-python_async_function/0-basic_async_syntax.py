#!/usr/bin/env python3
"""
The basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and
    max_delay seconds and eventually returns it.
    :param max_delay:
    :return:
    """
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
