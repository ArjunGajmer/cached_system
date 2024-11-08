import datetime
import logging
from typing import Dict, Tuple, Union

from cache_system.datastructure.data import CacheData
from cache_system.datastructure.double_linked_list import LinkedListNode, DoubleLinkedList
from cache_system.strategy.eviction.base import BaseEvictionBasedCacheStrategy


class TTlCacheStrategy(BaseEvictionBasedCacheStrategy):
    def __init__(self, capacity, ttl_period=2):
        super().__init__(capacity=capacity)
        self.__ttl_period = ttl_period
        self._data: Dict[str, Tuple[LinkedListNode, datetime.datetime]] = {}
        self._dl = DoubleLinkedList(capacity=capacity)

    @property
    def ttl_period(self):
        return self.__ttl_period

    @ttl_period.setter
    def ttl_period(self, ttl_period):
        self.__ttl_period = ttl_period

    def evict(self):
        self.__remove_expired()
        if self._dl.is_full():
            logging.debug(f"\n\n{'*' * 50}\n\n\t\tCache is Full ATM")
            raise f"Cache Is Full"

    def insert(self, key: Union[int, str], value: Union[int, str]):
        if self._dl.is_full():
            self.evict()
        node = LinkedListNode(CacheData(key=key, value=value))
        self._dl.insert_at_last(node)
        self._data[key] = (node, datetime.datetime.now() + datetime.timedelta(seconds=self.__ttl_period))

    def get_value(self, key: Union[int, str]) -> Union[int, str]:
        return self.__get_node(key).data.value

    def update_value(self, key: Union[int, str], value: Union[int, str]):
        node, expire_at = self._data[key]
        node.data.value = value

    def cached_data_exits(self, key: Union[int, str]) -> bool:
        present = key in self._data
        if present:
            self.__refresh_data_position(key)
        return present

    def __remove_expired(self):
        ptr = self._dl.get_head()
        while ptr and self.__expired(ptr.data.key):
            next_node = ptr.next_node
            self._dl.remove_node(ptr)
            self._data.pop(ptr.data.key)
            ptr = next_node

    def __refresh_data_position(self, key: Union[int, str]):
        node, _ = self._data[key]
        node = self._dl.remove_node(node)
        self._dl.insert_at_last(node)
        expire_at = datetime.datetime.now() + datetime.timedelta(seconds=self.__ttl_period)
        self._data[key] = (node, expire_at)
        return node

    def __get_node(self, key: Union[int, str]) -> LinkedListNode:
        return self._data[key][0]

    def __get_expire_at(self, key: Union[int, str]) -> datetime.datetime:
        return self._data[key][1]

    def __expired(self, key: Union[int, str]):
        return self.__get_expire_at(key) < datetime.datetime.now()

    def flush(self):
        self._data = {}
        self._dl.clear()

    def __str__(self):
        d = "\n".join(
            [f"{key}->{node.data.value}, Exp:{(expiration - datetime.datetime.now()).total_seconds()}"
             for key, (node, expiration) in self._data.items()]

        )
        return f"\nItems in Cache:\n{'*' * 15}\n{d}\n{'*' * 15}\n"
