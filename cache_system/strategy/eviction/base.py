import abc

from cache_system.strategy.base import BaseCacheStrategy


class BaseEvictionBasedCacheStrategy(BaseCacheStrategy, abc.ABC):

    @abc.abstractmethod
    def evict(self):
        pass
