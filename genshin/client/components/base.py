"""Base ABC Client."""

import abc
import base64
import functools
import json
import logging
import os
import typing
import urllib.parse
import warnings

import aiohttp.typedefs
import multidict
import yarl

from genshin import constants, errors, types, utility
from genshin.client import cache as client_cache
from genshin.client import routes
from genshin.client.manager import managers
from genshin.models import hoyolab as hoyolab_models
from genshin.utility import concurrency, deprecation, ds
from genshin.utility.uid import recognize_server

__all__ = ["BaseClient"]


T = typing.TypeVar("T")
CallableT = typing.TypeVar("CallableT", bound="typing.Callable[..., object]")
AsyncCallableT = typing.TypeVar("AsyncCallableT", bound="typing.Callable[..., typing.Awaitable[object]]")


def parse_loose_headers(
    loose_headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
) -> multidict.CIMultiDict[str]:
    """Parse loose aiohttp headers."""
    pass


class BaseClient(abc.ABC):
    """Base ABC Client."""

    __slots__ = (
        "cookie_manager",
        "cache",
        "_lang",
        "_region",
        "_default_game",
        "uids",
        "authkeys",
        "_hoyolab_id",
        "_accounts",
        "custom_headers",
    )

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"  # noqa: E501

    logger: logging.Logger = logging.getLogger(__name__)

    cookie_manager: managers.BaseCookieManager
    cache: client_cache.BaseCache
    _lang: str
    _region: types.Region
    _default_game: typing.Optional[types.Game]

    uids: dict[types.Game, int]
    authkeys: dict[types.Game, str]
    _hoyolab_id: typing.Optional[int]
    _accounts: dict[types.Game, hoyolab_models.GenshinAccount]
    custom_headers: multidict.CIMultiDict[str]

    def __init__(
        self,
        cookies: typing.Optional[managers.AnyCookieOrHeader] = None,
        *,
        authkey: typing.Optional[str] = None,
        lang: types.Lang = "en-us",
        region: types.Region = types.Region.OVERSEAS,
        proxy: typing.Optional[str] = None,
        game: typing.Optional[types.Game] = None,
        uid: typing.Optional[int] = None,
        hoyolab_id: typing.Optional[int] = None,
        device_id: typing.Optional[str] = None,
        device_fp: typing.Optional[str] = None,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        cache: typing.Optional[client_cache.BaseCache] = None,
        debug: bool = False,
    ) -> None:
        self.cookie_manager = managers.BaseCookieManager.from_cookies(cookies)
        self.cache = cache or client_cache.StaticCache()

        self.uids = {}
        self.authkeys = {}
        self._accounts = {}

        self.default_game = game
        self.lang = lang
        self.region = region
        self.authkey = authkey
        self.debug = debug
        self.proxy = proxy
        self.uid = uid
        self.hoyolab_id = hoyolab_id

        self.custom_headers = parse_loose_headers(headers)
        self.custom_headers.update({"x-rpc-device_id": device_id} if device_id else {})
        self.custom_headers.update({"x-rpc-device_fp": device_fp} if device_fp else {})

    def __repr__(self) -> str:
        kwargs = dict(
            lang=self.lang,
            region=self.region.value,
            default_game=self.default_game and self.default_game.value,
            hoyolab_id=self.hoyolab_id,
            uid=self.default_game and self.uid,
            authkey=self.authkey and self.authkey[:12] + "...",
            proxy=self.proxy,
            debug=self.debug,
        )
        return f"<{type(self).__name__} {', '.join(f'{k}={v!r}' for k, v in kwargs.items() if v)}>"

    @property
    def device_id(self) -> typing.Optional[str]:
        """The device id used in headers."""
        pass

    @device_id.setter
    def device_id(self, device_id: str) -> None:
        pass

    @property
    def device_fp(self) -> typing.Optional[str]:
        """The device fingerprint used in headers."""
        pass

    @device_fp.setter
    def device_fp(self, device_fp: str) -> None:
        pass

    @property
    def hoyolab_id(self) -> typing.Optional[int]:
        """The logged-in user's hoyolab uid.

        Returns None if not found or not applicable.
        """
        pass

    @hoyolab_id.setter
    def hoyolab_id(self, hoyolab_id: typing.Optional[int]) -> None:
        pass

    @property
    def lang(self) -> str:
        """The default language, defaults to "en-us" """
        pass

    @lang.setter
    def lang(self, lang: str) -> None:
        pass

    @property
    def region(self) -> types.Region:
        """The default region."""
        pass

    @region.setter
    def region(self, region: str) -> None:
        pass

    @property
    def default_game(self) -> typing.Optional[types.Game]:
        """The default game."""
        pass

    @default_game.setter
    def default_game(self, game: typing.Optional[str]) -> None:
        pass

    game = default_game

    @property
    def uid(self) -> typing.Optional[int]:
        """UID of the default game."""
        pass

    @uid.setter
    def uid(self, uid: typing.Optional[int]) -> None:
        pass

    @property
    def authkey(self) -> typing.Optional[str]:
        """The default genshin authkey used for paginators."""
        pass

    @authkey.setter
    def authkey(self, authkey: typing.Optional[str]) -> None:
        pass

    @property
    def debug(self) -> bool:
        """Whether the debug logs are being shown in stdout"""
        pass

    @debug.setter
    def debug(self, debug: bool) -> None:
        pass

    def set_cookies(self, cookies: typing.Optional[managers.AnyCookieOrHeader] = None, **kwargs: typing.Any) -> None:
        """Parse and set cookies."""
        pass

    def set_browser_cookies(self, browser: typing.Optional[str] = None) -> None:
        """Extract cookies from your browser and set them as client cookies.

        Available browsers: chrome, chromium, opera, edge, firefox.
        """
        pass

    def set_authkey(self, authkey: typing.Optional[str] = None, *, game: typing.Optional[types.Game] = None) -> None:
        """Set an authkey for wish & transaction logs.

        Accepts an authkey, a url containing an authkey or a path towards a logfile.
        """
        pass

    def set_cache(
        self, maxsize: int = 1024, *, ttl: int = client_cache.HOUR, static_ttl: int = client_cache.DAY
    ) -> None:
        """Create and set a new cache."""
        pass

    def set_redis_cache(
        self, url: str, *, ttl: int = client_cache.HOUR, static_ttl: int = client_cache.DAY, **redis_kwargs: typing.Any
    ) -> None:
        """Create and set a new redis cache."""
        pass

    @property
    def proxy(self) -> typing.Optional[str]:
        """Proxy for http requests."""
        pass

    @proxy.setter
    def proxy(self, proxy: typing.Optional[aiohttp.typedefs.StrOrURL]) -> None:
        pass

    async def _request_hook(
        self,
        method: str,
        url: aiohttp.typedefs.StrOrURL,
        *,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        data: typing.Any = None,
        **kwargs: typing.Any,
    ) -> None:
        """Perform an action before a request.

        Debug logging by default.
        """
        pass

    async def request(
        self,
        url: aiohttp.typedefs.StrOrURL,
        *,
        method: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        data: typing.Any = None,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        cache: typing.Any = None,
        static_cache: typing.Any = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request and return a parsed json response."""
        pass

    async def request_webstatic(
        self,
        url: aiohttp.typedefs.StrOrURL,
        *,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        cache: typing.Any = None,
        region: types.Region = types.Region.OVERSEAS,
        **kwargs: typing.Any,
    ) -> typing.Any:
        """Request a static json file."""
        pass

    async def request_bbs(
        self,
        url: aiohttp.typedefs.StrOrURL,
        *,
        lang: typing.Optional[str] = None,
        region: typing.Optional[types.Region] = None,
        method: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        data: typing.Any = None,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request any bbs endpoint."""
        pass

    async def request_hoyolab(
        self,
        url: aiohttp.typedefs.StrOrURL,
        *,
        lang: typing.Optional[str] = None,
        region: typing.Optional[types.Region] = None,
        method: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        data: typing.Any = None,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request any hoyolab endpoint."""
        pass

    @managers.no_multi
    async def get_game_accounts(
        self, *, lang: typing.Optional[str] = None
    ) -> typing.Sequence[hoyolab_models.GenshinAccount]:
        """Get the game accounts of the currently logged-in user."""
        pass

    @deprecation.deprecated("get_game_accounts")
    async def genshin_accounts(
        self, *, lang: typing.Optional[str] = None
    ) -> typing.Sequence[hoyolab_models.GenshinAccount]:
        """Get the genshin accounts of the currently logged-in user."""
        pass

    async def _update_cached_uids(self) -> None:
        """Update cached fallback uids."""
        pass

    @concurrency.prevent_concurrency
    async def _get_uid(self, game: types.Game) -> int:
        """Get a cached fallback uid."""
        pass

    async def _update_cached_accounts(self) -> None:
        """Update cached fallback accounts."""
        pass

    @concurrency.prevent_concurrency
    async def _get_account(self, game: types.Game) -> hoyolab_models.GenshinAccount:
        """Get a cached fallback account."""
        pass

    def _get_hoyolab_id(self) -> int:
        """Get a cached fallback hoyolab ID."""
        pass

    def get_account_timezone(
        self, *, game: typing.Optional[types.Game] = None, uid: typing.Optional[int] = None
    ) -> typing.Optional[int]:
        """Get the UTC timezone of the default game account."""
        pass

    def _add_timezone_to_data(
        self,
        data: typing.Mapping[str, typing.Any],
        keys: typing.Sequence[str],
        *,
        game: typing.Optional[types.Game] = None,
        uid: typing.Optional[int] = None,
    ) -> typing.Mapping[str, typing.Any]:
        """Add timezone info to a data dict based on the default game account."""
        pass


def region_specific(region: types.Region) -> typing.Callable[[AsyncCallableT], AsyncCallableT]:
    """Prevent function to be ran with unsupported regions."""

    def decorator(func: AsyncCallableT) -> AsyncCallableT:
        return func

    return decorator
