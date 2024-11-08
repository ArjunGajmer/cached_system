from typing import Dict, Union

from cache_system.datastructure.data import CacheData
from cache_system.datastructure.double_linked_list import DoubleLinkedList, LinkedListNode
from cache_system.strategy.base import BaseCacheStrategy


class LRUCacheStrategy(BaseCacheStrategy):

    def __init__(self, capacity: int):
        super().__init__(capacity=capacity)
        self._data: Dict[str, LinkedListNode] = {}
        self._dl = DoubleLinkedList(capacity=capacity)

    def evict(self):
        node: LinkedListNode = self._dl.remove_head()
        self._data.pop(node.data.key)

    def insert(self, key: Union[int, str], value: Union[int, str]):
        if self._dl.is_full():
            self.evict()
        node = LinkedListNode(CacheData(key=key, value=value))
        self._dl.insert_at_last(node)
        self._data[key] = node

    def get_value(self, key: Union[int, str]) -> Union[int, str]:
        return self._data[key].data.value

    def update_value(self, key: Union[int, str], value: Union[int, str]):
        node: LinkedListNode = self._data[key]
        node.data.value = value

    def cached_data_exits(self, key: Union[int, str]) -> bool:
        present = key in self._data
        if present:
            self.__refresh_data_position(key)
        return present

    def flush(self):
        self._data = {}
        self._dl.clear()

    def __refresh_data_position(self, key: Union[int, str]):
        node: LinkedListNode = self._data[key]
        node = self._dl.remove_node(node)
        self._dl.insert_at_last(node)

    def __str__(self):
        d = "\n".join([f"{key}->{node.data.value}" for key, node in self._data.items()])
        return f"\nItem in Cache:\n{'*' * 15}\n{d}\n{'*' * 15}\n"
