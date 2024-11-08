import logging
import os
import sys

sys.path.append(os.path.abspath('../cache_system'))

from cache_system.cache import Cache
from cache_system.factory import CacheGenerator

log_file_path = os.path.join('logs', 'lfu_simulation.log')
if os.path.exists(log_file_path):
    os.remove(log_file_path)

logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def run_lfu_simulation():
    capacity = 4
    cache: Cache = CacheGenerator.get('lfu', capacity=capacity)

    logging.debug(f"Cache Capacity:{capacity}\n")

    cache.insert(1, 117)
    cache.insert(2, 127)
    cache.insert(3, 137)
    cache.get_value(1)

    logging.debug(cache)

    cache.insert(2, 122)
    logging.debug(cache)

    cache.insert(7, 177)
    logging.debug(cache)

    cache.insert(4, 148)
    logging.debug(cache)

    cache.get_value(4)
    logging.debug(cache)

    cache.get_value(1)
    cache.get_value(2)
    cache.get_value(4)
    logging.debug(cache)

    cache.insert(10, 1107)
    cache.get_value(10)
    logging.debug(cache)

    cache.insert(11, 1117)
    logging.debug(cache)
    cache.flush()


if __name__ == '__main__':
    run_lfu_simulation()
