"""Cookie completion.

Available conversions:

- fetch_cookie_with_cookie
    - cookie_token -> cookie_token
    - cookie_token -> ltoken
    - stoken -> cookie_token
    - stoken -> ltoken
    - stoken -> login_ticket
- fetch_cookie_token_info
    - cookie_token -> cookie_token
    - login_ticket -> cookie_token
- fetch_cookie_with_stoken_v2
    - stoken (v2) + mid -> ltoken_v2 (token_type=2)
    - stoken (v2) + mid -> cookie_token_v2 (token_type=4)
- cn_fetch_cookie_token_with_stoken_v2
    - stoken (v2) + mid -> cookie_token
- fetch_cookie_token_with_game_token
    - game_token -> cookie_token
- fetch_stoken_with_game_token
    - game_token -> stoken
"""

from __future__ import annotations

import random
import typing
import uuid
from string import ascii_letters, digits

import aiohttp

from genshin import constants, errors, types
from genshin.client import routes
from genshin.client.manager import managers
from genshin.models.auth.cookie import StokenResult
from genshin.utility import ds as ds_utility

__all__ = [
    "cn_fetch_cookie_token_with_stoken_v2",
    "complete_cookies",
    "fetch_cookie_token_info",
    "fetch_cookie_token_with_game_token",
    "fetch_cookie_with_cookie",
    "fetch_cookie_with_stoken_v2",
    "fetch_stoken_with_game_token",
    "refresh_cookie_token",
]


async def fetch_cookie_with_cookie(
    cookies: managers.CookieOrHeader,
    *,
    source: typing.Literal["CookieToken", "SToken"],
    target: typing.Literal["CookieAccountInfo", "LToken", "ActionTicket"],
    region: types.Region = types.Region.OVERSEAS,
) -> typing.Mapping[str, str]:
    """Fetch cookie token info with an stoken."""
    pass


async def fetch_cookie_with_stoken_v2(
    cookies: managers.CookieOrHeader,
    *,
    token_types: list[typing.Literal[2, 4]],
) -> typing.Mapping[str, str]:
    """Fetch cookie (v2) with an stoken (v2) and mid."""
    pass


async def cn_fetch_cookie_token_with_stoken_v2(
    cookies: managers.CookieOrHeader,
) -> typing.Mapping[typing.Literal["uid", "cookie_token"], str]:
    """Fetch cookie_token with an stoken (v2) and mid."""
    pass


async def fetch_cookie_token_info(
    cookies: managers.CookieOrHeader,
    *,
    source: typing.Literal["cookie_token", "login_ticket"],
    region: types.Region = types.Region.OVERSEAS,
) -> typing.Mapping[str, typing.Any]:
    """Fetch cookie token info."""
    pass


async def refresh_cookie_token(
    cookies: managers.CookieOrHeader,
    *,
    source: typing.Literal["cookie_token", "login_ticket"] = "cookie_token",
    region: types.Region = types.Region.OVERSEAS,
) -> typing.MutableMapping[str, str]:
    """Refresh a cookie token to make it last longer."""
    pass


async def complete_cookies(
    cookies: managers.CookieOrHeader,
    *,
    refresh: bool = True,
    region: types.Region = types.Region.OVERSEAS,
) -> typing.Mapping[str, str]:
    """Add ltoken and ltuid to a cookie with only a cookie_token and an account_id.

    If refresh is True, the cookie token will be refreshed to last longer.
    """
    pass


async def fetch_cookie_token_with_game_token(*, game_token: str, account_id: str) -> str:
    """Fetch cookie token with game token, which can be obtained by scanning a QR code."""
    pass


async def fetch_stoken_with_game_token(*, game_token: str, account_id: int) -> StokenResult:
    """Fetch cookie token with game token, which can be obtained by scanning a QR code."""
    pass
