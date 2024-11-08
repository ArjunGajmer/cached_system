from typing import Union

from cache_system.datastructure.data import CacheData


class LinkedListNode:
    def __init__(self, data: CacheData, prev_node=None, nex_node=None):
        self.next_node: Union[LinkedListNode | None] = nex_node
        self.prev_node: Union[LinkedListNode | None] = prev_node
        self.data: CacheData = data


class DoubleLinkedList:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self._head: Union[LinkedListNode | None] = None
        self._tail: Union[LinkedListNode | None] = None
        self.__current_capacity: int = 0

    def insert_at_last(self, node: LinkedListNode) -> LinkedListNode:
        if self.is_empty():
            self._head = node
        else:
            self._tail.next_node = node
            node.prev_node = self._tail
        self._tail = node
        self.__current_capacity += 1
        return node

    def remove_node(self, node: LinkedListNode) -> LinkedListNode:
        if node == self._head == self._tail:
            self._tail = self._head = None

        elif node == self._head:
            self._head = node.next_node

        elif node == self._tail:
            self._tail = node.prev_node

        else:
            prev_node, next_node = node.prev_node, node.next_node
            prev_node.next_node = next_node
            next_node.prev_node = prev_node

        self.__current_capacity -= 1
        node.prev_node = None
        node.next_node = None
        return node

    def remove_head(self) -> LinkedListNode:
        return self.remove_node(self._head)

    def is_full(self) -> bool:
        return self.capacity == self.__current_capacity

    @staticmethod
    def update_data(node: LinkedListNode, data: CacheData):
        node.data = data
        return node

    def get_head(self):
        return self._head

    def clear(self):
        self._tail = self._head = None
        self.__current_capacity = 0

    def is_empty(self):
        return self._head is None and self._tail is None
