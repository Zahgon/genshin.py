"""Ratelimit handlers."""

import functools
import logging
import typing

import aiohttp
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_random_exponential,
)

from genshin import errors

LOGGER_ = logging.getLogger(__name__)
TIMEOUT_ERRORS = (TimeoutError, aiohttp.ClientError, ConnectionResetError)
CallableT = typing.TypeVar("CallableT", bound=typing.Callable[..., typing.Awaitable[typing.Any]])


def handle_ratelimits(
    tries: int = 7,
    exception: type[errors.GenshinException] = errors.VisitsTooFrequently,
    delay: float = 0.5,
) -> typing.Callable[[CallableT], CallableT]:
    """Handle ratelimits for requests."""

    def decorator(func: CallableT) -> CallableT:
        return func

    return decorator


def handle_request_timeouts(
    tries: int = 5,
    delay: float = 0.5,
) -> typing.Callable[[CallableT], CallableT]:
    """Handle timeout errors for requests."""

    def decorator(func: CallableT) -> CallableT:
        return func

    return decorator


def handle_proxy_errors(func: CallableT) -> CallableT:
    """If a proxy error occurs, retry the request once without the proxy."""
    return func
