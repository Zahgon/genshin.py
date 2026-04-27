"""Cookie managers for making authenticated requests."""

from __future__ import annotations

import abc
import functools
import http.cookies
import logging
import typing
import warnings

import aiohttp
import aiohttp.typedefs
import yarl

from genshin import errors, types
from genshin.client import ratelimit
from genshin.utility import fs as fs_utility

_LOGGER = logging.getLogger(__name__)

__all__ = [
    "BaseCookieManager",
    "CookieManager",
    "InternationalCookieManager",
    "RawResponse",
    "RotatingCookieManager",
    "parse_cookie",
]

CookieOrHeader = typing.Union["http.cookies.BaseCookie[typing.Any]", typing.Mapping[typing.Any, typing.Any], str]
AnyCookieOrHeader = typing.Union[CookieOrHeader, typing.Sequence[CookieOrHeader]]

T = typing.TypeVar("T")
CallableT = typing.TypeVar("CallableT", bound="typing.Callable[..., object]")
AsyncCallableT = typing.TypeVar("AsyncCallableT", bound="typing.Callable[..., typing.Awaitable[object]]")
MaybeSequence = typing.Union[T, typing.Sequence[T]]


def parse_cookie(cookie: typing.Optional[CookieOrHeader]) -> dict[str, str]:
    """Parse a cookie or header into a cookie mapping."""
    pass


def get_cookie_identifier(cookie: typing.Mapping[str, str]) -> typing.Optional[str]:
    """Get a unique identifier for a cookie."""
    pass


class RawResponse(typing.NamedTuple):
    """Raw HTTP response for auth endpoints that need headers/cookies."""

    data: typing.Any
    headers: typing.Any
    cookies: http.cookies.SimpleCookie


class BaseCookieManager(abc.ABC):
    """A cookie manager for making requests."""

    _proxy: typing.Optional[yarl.URL] = None
    _socks_proxy: typing.Optional[str] = None

    @classmethod
    def from_cookies(cls, cookies: typing.Optional[AnyCookieOrHeader] = None) -> BaseCookieManager:
        """Create an arbitrary cookie manager implementation instance."""
        pass

    @classmethod
    def from_browser_cookies(cls, browser: typing.Optional[str] = None) -> CookieManager:
        """Create a cookie manager with browser cookies."""
        pass

    @property
    def available(self) -> bool:
        """Whether the authentication cookies are available."""
        pass

    @property
    def multi(self) -> bool:
        """Whether the cookie manager contains multiple cookies and therefore should not cache private data."""
        pass

    @property
    def user_id(self) -> typing.Optional[int]:
        """The id of the user that owns cookies.

        Returns None if not found or not applicable.
        """
        pass

    @property
    def proxy(self) -> typing.Optional[yarl.URL]:
        """Proxy for http(s) requests."""
        pass

    @proxy.setter
    def proxy(self, proxy: typing.Optional[aiohttp.typedefs.StrOrURL]) -> None:
        pass

    def create_session(self, **kwargs: typing.Any) -> aiohttp.ClientSession:
        """Create a client session."""
        pass

    @ratelimit.handle_ratelimits()
    @ratelimit.handle_proxy_errors
    @ratelimit.handle_request_timeouts()
    async def _request(
        self,
        method: str,
        str_or_url: aiohttp.typedefs.StrOrURL,
        cookies: typing.MutableMapping[str, str],
        **kwargs: typing.Any,
    ) -> typing.Any:
        """Make a request towards any json resource."""
        pass

    @ratelimit.handle_ratelimits()
    @ratelimit.handle_proxy_errors
    @ratelimit.handle_request_timeouts()
    async def _raw_request(
        self,
        method: str,
        str_or_url: aiohttp.typedefs.StrOrURL,
        *,
        cookies: typing.Optional[typing.Mapping[str, str]] = None,
        **kwargs: typing.Any,
    ) -> RawResponse:
        """Make a request and return data + headers + cookies (no retcode enforcement)."""
        pass

    @abc.abstractmethod
    async def request(
        self,
        url: aiohttp.typedefs.StrOrURL,
        *,
        method: str = "GET",
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        data: typing.Any = None,
        json: typing.Any = None,
        cookies: typing.Optional[aiohttp.typedefs.LooseCookies] = None,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        **kwargs: typing.Any,
    ) -> typing.Any:
        """Make an authenticated request."""


class CookieManager(BaseCookieManager):
    """Standard implementation of the cookie manager."""

    _cookies: dict[str, str]

    def __init__(
        self,
        cookies: typing.Optional[CookieOrHeader] = None,
    ) -> None:
        self.cookies = parse_cookie(cookies)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.cookies})"

    @property
    def cookies(self) -> typing.MutableMapping[str, str]:
        """Cookies used for authentication."""
        pass

    @cookies.setter
    def cookies(self, cookies: typing.Optional[CookieOrHeader]) -> None:
        pass

    @property
    def available(self) -> bool:
        pass

    @property
    def multi(self) -> bool:
        pass

    @property
    def jar(self) -> http.cookies.SimpleCookie:
        """SimpleCookie containing the cookies."""
        pass

    @property
    def header(self) -> str:
        """Header representation of cookies.

        This representation is reparsable by the manager.
        """
        pass

    def set_cookies(
        self,
        cookies: typing.Optional[CookieOrHeader] = None,
        **kwargs: typing.Any,
    ) -> typing.MutableMapping[str, str]:
        """Parse and set cookies."""
        pass

    def set_browser_cookies(self, browser: typing.Optional[str] = None) -> typing.Mapping[str, str]:
        """Extract cookies from your browser and set them as client cookies.

        Available browsers: chrome, chromium, opera, edge, firefox.
        """
        pass

    @property
    def user_id(self) -> typing.Optional[int]:
        """The id of the user that owns cookies.

        Returns None if cookies are not set.
        """
        pass

    async def request(
        self,
        url: aiohttp.typedefs.StrOrURL,
        *,
        method: str = "GET",
        **kwargs: typing.Any,
    ) -> typing.Any:
        """Make an authenticated request."""
        pass


class CookieSequence(typing.Sequence[typing.Mapping[str, str]]):
    MAX_USES: int = 30

    # {id: ({cookie}, uses), ...}
    _cookies: dict[str, tuple[dict[str, str], int]]

    def __init__(self, cookies: typing.Optional[typing.Sequence[CookieOrHeader]] = None) -> None:
        self.cookies = [parse_cookie(cookie) for cookie in cookies or []]

    @property
    def cookies(self) -> typing.Sequence[typing.Mapping[str, str]]:
        """Cookies used for authentication"""
        pass

    @cookies.setter
    def cookies(self, cookies: typing.Optional[typing.Sequence[CookieOrHeader]]) -> None:
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} len={len(self._cookies)}>"

    def __getitem__(self, index: int) -> typing.Mapping[str, str]:  # type: ignore # I can't be fucked with slices
        return self.cookies[index]

    def __len__(self) -> int:
        return len(self.cookies)

    def __iter__(self) -> typing.Iterator[typing.Mapping[str, str]]:
        return iter(self.cookies)


class RotatingCookieManager(BaseCookieManager):
    """Cookie Manager with rotating cookies."""

    _cookies: CookieSequence

    def __init__(self, cookies: typing.Optional[typing.Sequence[CookieOrHeader]] = None) -> None:
        self.set_cookies(cookies)

    @property
    def cookies(self) -> typing.Sequence[typing.Mapping[str, str]]:
        """Cookies used for authentication"""
        pass

    @cookies.setter
    def cookies(self, cookies: typing.Optional[typing.Sequence[CookieOrHeader]]) -> None:
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} len={len(self._cookies)}>"

    @property
    def available(self) -> bool:
        pass

    @property
    def multi(self) -> bool:
        pass

    def set_cookies(
        self,
        cookies: typing.Optional[typing.Sequence[CookieOrHeader]] = None,
    ) -> typing.Sequence[typing.Mapping[str, str]]:
        """Parse and set cookies."""
        pass

    async def request(
        self,
        url: aiohttp.typedefs.StrOrURL,
        *,
        method: str = "GET",
        **kwargs: typing.Any,
    ) -> typing.Any:
        """Make an authenticated request."""
        pass


class InternationalCookieManager(BaseCookieManager):
    """Cookie Manager with international rotating cookies."""

    _cookies: typing.Mapping[types.Region, CookieSequence]

    def __init__(self, cookies: typing.Optional[typing.Mapping[str, MaybeSequence[CookieOrHeader]]] = None) -> None:
        self.set_cookies(cookies)

    @property
    def cookies(self) -> typing.Mapping[types.Region, typing.Sequence[typing.Mapping[str, str]]]:
        """Cookies used for authentication"""
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"

    @property
    def available(self) -> bool:
        pass

    @property
    def multi(self) -> bool:
        pass

    def set_cookies(
        self,
        cookies: typing.Optional[typing.Mapping[str, MaybeSequence[CookieOrHeader]]] = None,
    ) -> typing.Mapping[types.Region, typing.Sequence[typing.Mapping[str, str]]]:
        """Parse and set cookies."""
        pass

    def guess_region(self, url: yarl.URL) -> types.Region:
        """Guess the region from the URL."""
        pass

    async def request(
        self,
        url: aiohttp.typedefs.StrOrURL,
        *,
        method: str = "GET",
        **kwargs: typing.Any,
    ) -> typing.Any:
        """Make an authenticated request."""
        pass


def no_multi(func: CallableT) -> CallableT:
    """Prevent function to be ran with a multi-cookie manager."""
    pass


def requires_cookie_token(func: AsyncCallableT) -> AsyncCallableT:
    """Prevent function to be ran without a cookie_token."""
    pass
