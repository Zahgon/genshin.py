"""File system related utilities."""

import functools
import pathlib
import tempfile
import typing

__all__ = ["get_browser_cookies"]

DOMAINS: typing.Final[typing.Sequence[str]] = ("mihoyo", "hoyolab", "hoyoverse")
ALLOWED_COOKIES: typing.Final[typing.Sequence[str]] = (
    "ltuid",
    "ltoken",
    "account_id",
    "cookie_token",
    "ltoken_v2",
    "ltmid_v2",
    "cookie_token_v2",
    "account_mid_v2",
)


def _get_browser_cookies(
    browser: typing.Optional[str] = None,
    *,
    cookie_file: typing.Optional[str] = None,
    domains: typing.Optional[typing.Sequence[str]] = None,
) -> typing.Mapping[str, str]:
    """Get cookies using browser-cookie3 from several domains.

    Available browsers: chrome, chromium, opera, edge, firefox.
    """
    pass


def get_browser_cookies(
    browser: typing.Optional[str] = None,
    *,
    cookie_file: typing.Optional[str] = None,
    domains: typing.Sequence[str] = DOMAINS,
    allowed_cookies: typing.Sequence[str] = ALLOWED_COOKIES,
) -> typing.Mapping[str, str]:
    """Get hoyolab authentication cookies from your browser for later storing.

    Available browsers: chrome, chromium, opera, edge, firefox.
    """
    pass


def get_tempdir() -> pathlib.Path:
    """Get the temporary directory to be used by genshin.py."""
    return pathlib.Path(tempfile.gettempdir()) / "genshin.py"


if __name__ == "__main__":
    print(get_browser_cookies("chrome"))  # noqa
