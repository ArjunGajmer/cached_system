from typing import Union

from pydantic import BaseModel


class CacheData(BaseModel):
    value: Union[str, int]
    key: Union[str, int]


class FrequencyBasedCachedData(CacheData):
    freq: int = 1
