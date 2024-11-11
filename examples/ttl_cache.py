import logging
import os
import time
import sys

sys.path.append(os.path.abspath('../cache_system'))

from cache_system.cache import Cache
from cache_system.factory import CacheGenerator

log_file_path = os.path.join('logs', 'ttl_simulation.log')
if os.path.exists(log_file_path):
    os.remove(log_file_path)

logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def run_ttl_simulation():
    capacity = 4
    ttl_period = 2
    cache: Cache = CacheGenerator.get('ttl', capacity=capacity)
    cache.cache_strategy.ttl_period = ttl_period

    logging.debug(f"Cache Capacity:{capacity} and ttl: {ttl_period}\n")
    cache.insert(1, 101)
    cache.insert(2, 201)
    cache.insert(3, 301)
    cache.insert(4, 400)
    logging.debug(cache)

    logging.debug(f"\nAfter {1} second\n")
    time.sleep(ttl_period + 1)
    cache.get_value(2)
    logging.debug(cache)


    logging.debug(f"\nAfter {ttl_period + 1} second\n")
    time.sleep(ttl_period + 1)
    cache.insert(5, 500)
    logging.debug(cache)

    logging.debug(f"\nAfter {1} second\n")
    time.sleep(1)
    cache.insert(6, 600)
    logging.debug(cache)

    logging.debug(f"\nAfter {1} second\n")
    time.sleep(1)
    cache.insert(7, 700)
    logging.debug(cache)

    logging.debug(f"\nAfter {1} second\n")
    time.sleep(1)
    cache.insert(8, 800)
    logging.debug(cache)

    logging.debug(f"\nAfter {1} second\n")
    time.sleep(1)
    cache.get_value(5)
    logging.debug(cache)

    logging.debug(f"\nAfter {1} second\n")
    time.sleep(1)
    cache.insert(1, 10)
    logging.debug(cache)

    cache.insert(11, 10)
    cache.insert(12, 10)
    logging.debug(cache)

    cache.insert(13, 10)
    cache.insert(14, 10)
    cache.insert(15, 10)
    cache.flush()


if __name__ == '__main__':
    run_ttl_simulation()
