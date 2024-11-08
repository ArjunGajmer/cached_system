import logging
from typing import Union

from cache_system.strategy.base import BaseCacheStrategy


class Cache:
    def __init__(self, cache_strategy: BaseCacheStrategy):
        self.cache_strategy: BaseCacheStrategy = cache_strategy

    def insert(self, key: Union[int, str], value: Union[int, str]):
        logging.debug(f"Inserting: key {key} with value: {value}")
        if self.cache_strategy.cached_data_exits(key):
            self.cache_strategy.update_value(key, value)
            return
        self.cache_strategy.insert(key, value)

    def get_value(self, key: Union[int, str]) -> Union[int, str, None]:
        if self.cache_strategy.cached_data_exits(key):
            val = self.cache_strategy.get_value(key)
            logging.debug(f"Fetching value from cache with key {key}: {val}")
            return val
        return None

    def flush(self):
        self.cache_strategy.flush()

    def __str__(self):
        return str(self.cache_strategy)
