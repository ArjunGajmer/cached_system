from typing import Dict, Union
from cache_system.datastructure.data import FrequencyBasedCachedData
from cache_system.strategy.base import BaseCacheStrategy


class LFUCacheStrategy(BaseCacheStrategy):

    def __init__(self, capacity):
        super().__init__(capacity=capacity)
        self._data: Dict[str, FrequencyBasedCachedData] = {}
        self._freq_map: Dict[int, Dict[str, FrequencyBasedCachedData]] = {}
        self._min_frequency: float = float('inf')

    def evict(self):
        data_map: Union[Dict[str, FrequencyBasedCachedData], None] = self._freq_map.get(self._min_frequency)
        key, value = data_map.popitem()
        if not data_map:
            self._freq_map.pop(self._min_frequency)
        self._data.pop(key)

    def update_value(self, key: Union[int, str], value: Union[int, str]):
        self._data[key].value = value

    def insert(self, key: Union[int, str], value: Union[int, str]):
        if len(self._data) >= self.capacity:
            self.evict()
        data = FrequencyBasedCachedData(key=key, value=value)
        self._data[key] = data
        return self.__insert_data_node_frequency_map(data=data)

    def cached_data_exits(self, key: Union[int, str]) -> bool:
        if key in self._data:
            self.__refresh(key)
            return True
        return False

    def get_value(self, key: Union[int, str]) -> Union[int, str]:
        return self._data[key].value

    def __insert_data_node_frequency_map(self, data: FrequencyBasedCachedData):
        data_map: Union[Dict[str, FrequencyBasedCachedData], None] = self._freq_map.get(data.freq)
        if not data_map:
            data_map = {}
        data_map[data.key] = data
        self._freq_map[data.freq] = data_map
        self._min_frequency = min(data.freq, self._min_frequency)

    def __remove_node_from_freq_linked_list(self, data: FrequencyBasedCachedData):
        data_map: Union[Dict[str, FrequencyBasedCachedData], None] = self._freq_map.get(data.freq)
        if data_map and data_map.get(data.key):
            data_map.pop(data.key)
        if not self._freq_map.get(data.freq):
            self._freq_map.pop(data.freq)

    def __refresh(self, key):
        data: FrequencyBasedCachedData = self._data[key]
        self.__remove_node_from_freq_linked_list(data=data)
        if self._freq_map.get(data.freq) is None and self._min_frequency == data.freq:
            self._min_frequency = data.freq + 1
        data.freq += 1
        self.__insert_data_node_frequency_map(data=data)

    def flush(self):
        del self._data
        del self._freq_map
        del self._min_frequency
        self._data: Dict[str, FrequencyBasedCachedData] = {}
        self._freq_map: Dict[int, Dict[str, FrequencyBasedCachedData]] = {}
        self._min_frequency: float = float('inf')

    def __str__(self):
        d = "\n".join(
            f"freq-{freq}:{[(node.key, node.value) for node in nodes.values()]}"
            for freq, nodes in self._freq_map.items()
        )
        return f"\nItem in Cache:\n{'*' * 15}\n{d}\n{'*' * 15}\n"
