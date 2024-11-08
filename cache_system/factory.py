from typing import Dict, Type

from cache_system.cache import Cache
from cache_system.strategy.base import BaseCacheStrategy
from cache_system.strategy.eviction.lfu import LFUCacheStrategy
from cache_system.strategy.eviction.lru import LRUCacheStrategy
from cache_system.strategy.eviction.ttl import TTlCacheStrategy
from cache_system.strategy.non_eviction import NonEvictionBased


class CacheGenerator:
    CACHE_STRATEGY_MAP: Dict[str, Type[BaseCacheStrategy]] = {
        'lru': LRUCacheStrategy,
        'lfu': LFUCacheStrategy,
        'ttl': TTlCacheStrategy,
        'non_eviction': NonEvictionBased
    }

    @staticmethod
    def get(cache_strategy: str, capacity: int) -> Cache:
        strategy: Type[BaseCacheStrategy] = CacheGenerator.CACHE_STRATEGY_MAP.get(cache_strategy)
        return Cache(strategy(capacity=capacity))
