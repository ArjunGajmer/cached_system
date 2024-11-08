import abc
from typing import Union


class BaseCacheStrategy(abc.ABC):

    def __init__(self, capacity: int):
        self.capacity: int = capacity

    def __new__(cls, *args, **kwargs):
        capacity: int = kwargs.get('capacity')
        assert capacity > 0  # won't even allow to create object if capacity is less than 0
        return super().__new__(cls)

    @abc.abstractmethod
    def insert(self, key: Union[int, str], value: Union[int, str]):
        pass

    @abc.abstractmethod
    def cached_data_exits(self, key: Union[int, str]) -> bool:
        pass

    @abc.abstractmethod
    def update_value(self, key: Union[int, str], value: Union[int, str]):
        pass

    @abc.abstractmethod
    def get_value(self, key: Union[int, str]) -> Union[int, str]:
        pass

    @abc.abstractmethod
    def flush(self):
        pass
