import logging
from typing import Union

from cache_system.strategy.base import BaseCacheStrategy


class NonEvictionBased(BaseCacheStrategy):

    def __init__(self, capacity: int):
        super().__init__(capacity=capacity)
        self._data: [str, Union[str, int]] = {}

    def insert(self, key: Union[int, str], value: Union[int, str]):
        if len(self._data) >= self.capacity:
            logging.debug(f"\n\n{'*' * 50}\n\n\t\tCache is Full.Please flush it.")
            raise f"Cache Is Full"
        self._data[key] = value

    def cached_data_exits(self, key: Union[int, str]) -> bool:
        return key in self._data

    def update_value(self, key: Union[int, str], value: Union[int, str]):
        self._data[key] = value

    def get_value(self, key: Union[int, str]) -> Union[int, str]:
        return self._data[key]

    def flush(self):
        self._data.clear()

    def __str__(self):
        d = "\n".join([f"{key}->{node}" for key, node in self._data.items()])
        return f"\nItem in Cache:\n{'*' * 15}\n{d}\n{'*' * 15}\n"
