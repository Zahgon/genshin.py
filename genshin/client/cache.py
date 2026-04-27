"""Cache for client."""

from __future__ import annotations

import abc
import dataclasses
import enum
import json
import sys
import time
import typing

if typing.TYPE_CHECKING:
    import aioredis
    import aiosqlite


__all__ = ["BaseCache", "Cache", "RedisCache", "SQLiteCache", "StaticCache"]

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
WEEK = DAY * 7


def _separate(values: typing.Iterable[typing.Any], sep: str = ":") -> str:
    """Separate a sequence by a separator into a single string."""
    pass


@dataclasses.dataclass(eq=False)
class CacheKey:
    def __str__(self) -> str:
        values = [getattr(self, field.name) for field in dataclasses.fields(self)]
        return _separate(values)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, o: object) -> bool:
        return isinstance(o, CacheKey) and str(self) == str(o)


def cache_key(key: str, **kwargs: typing.Any) -> CacheKey:
    pass


class BaseCache(abc.ABC):
    """Base cache for the client."""

    @abc.abstractmethod
    async def get(self, key: typing.Any) -> typing.Optional[typing.Any]:
        """Get an object with a key."""

    @abc.abstractmethod
    async def set(self, key: typing.Any, value: typing.Any) -> None:
        """Save an object with a key."""

    @abc.abstractmethod
    async def get_static(self, key: typing.Any) -> typing.Optional[typing.Any]:
        """Get a static object with a key."""

    @abc.abstractmethod
    async def set_static(self, key: typing.Any, value: typing.Any) -> None:
        """Save a static object with a key."""


class Cache(BaseCache):
    """Standard implementation of the cache."""

    cache: dict[typing.Any, tuple[float, typing.Any]]
    maxsize: int
    ttl: float
    static_ttl: float

    def __init__(self, maxsize: int = 1024, *, ttl: float = HOUR, static_ttl: float = DAY) -> None:
        self.cache = {}
        self.maxsize = maxsize

        self.ttl = ttl
        self.static_ttl = static_ttl

    def __len__(self) -> int:
        self._clear_cache()
        return len(self.cache)

    def _clear_cache(self) -> None:
        """Clear timed-out items."""
        pass

    async def get(self, key: typing.Any) -> typing.Optional[typing.Any]:
        """Get an object with a key."""
        pass

    async def set(self, key: typing.Any, value: typing.Any) -> None:
        """Save an object with a key."""
        pass

    async def get_static(self, key: typing.Any) -> typing.Optional[typing.Any]:
        """Get a static object with a key."""
        pass

    async def set_static(self, key: typing.Any, value: typing.Any) -> None:
        """Save a static object with a key."""
        pass


class StaticCache(Cache):
    """Cache for only static resources."""

    def __init__(self, ttl: float = DAY) -> None:
        super().__init__(maxsize=sys.maxsize, ttl=0, static_ttl=ttl)

    async def set(self, key: typing.Any, value: typing.Any) -> None:
        """Do nothing."""


class RedisCache(BaseCache):
    """Redis implementation of the cache."""

    redis: aioredis.Redis
    ttl: int
    static_ttl: int

    def __init__(self, redis: aioredis.Redis, *, ttl: int = HOUR, static_ttl: int = DAY) -> None:
        self.redis = redis
        self.ttl = ttl
        self.static_ttl = static_ttl

    def serialize_key(self, key: typing.Any) -> str:
        """Serialize a key by turning it into a string."""
        pass

    def serialize_value(self, value: typing.Any) -> typing.Union[str, bytes]:
        """Serialize a value by turning it into bytes."""
        pass

    def deserialize_value(self, value: bytes) -> typing.Any:
        """Deserialize a value back into data."""
        pass

    async def get(self, key: typing.Any) -> typing.Optional[typing.Any]:
        """Get an object with a key."""
        pass

    async def set(self, key: typing.Any, value: typing.Any) -> None:
        """Save an object with a key."""
        pass

    async def get_static(self, key: typing.Any) -> typing.Optional[typing.Any]:
        """Get a static object with a key."""
        pass

    async def set_static(self, key: typing.Any, value: typing.Any) -> None:
        """Save a static object with a key."""
        pass


class SQLiteCache(BaseCache):
    """SQLite implementation of the cache."""

    conn: aiosqlite.Connection | None
    ttl: int
    static_ttl: int

    def __init__(
        self,
        conn: aiosqlite.Connection | None = None,
        *,
        ttl: int = HOUR,
        static_ttl: int = DAY,
        db_name: str = ".cache/genshin_py.db",
    ) -> None:
        self.conn = conn
        self.ttl = ttl
        self.static_ttl = static_ttl
        self.db_name = db_name

    async def _clear_cache(self, conn: aiosqlite.Connection) -> None:
        """Clear timed-out items."""
        pass

    async def initialize(self) -> None:
        """Initialize the cache."""
        pass

    def serialize_key(self, key: typing.Any) -> str:
        """Serialize a key by turning it into a string."""
        pass

    def serialize_value(self, value: typing.Any) -> str:
        """Serialize a value by turning it into a string."""
        pass

    def deserialize_value(self, value: str) -> typing.Any:
        """Deserialize a value back into data."""
        pass

    async def get(self, key: typing.Any) -> typing.Optional[typing.Any]:
        """Get an object with a key."""
        pass

    async def set(self, key: typing.Any, value: typing.Any) -> None:
        """Save an object with a key."""
        pass

    async def get_static(self, key: typing.Any) -> typing.Optional[typing.Any]:
        """Get a static object with a key."""
        pass

    async def set_static(self, key: typing.Any, value: typing.Any) -> None:
        """Save a static object with a key."""
        pass
