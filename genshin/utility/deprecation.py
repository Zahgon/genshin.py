"""Deprecation decorator."""

import functools
import inspect
import typing
import warnings

__all__ = ["deprecated", "warn_deprecated"]

CallableT = typing.TypeVar("CallableT", bound=typing.Callable[..., typing.Any])


def warn_deprecated(
    obj: typing.Any,
    *,
    alternative: typing.Optional[str] = None,
    stack_level: int = 3,
) -> None:
    """Raise a deprecated warning."""
    pass


def deprecated(alternative: typing.Optional[str] = None) -> typing.Callable[[CallableT], CallableT]:
    """Mark a function as deprecated."""

    def decorator(func: CallableT) -> CallableT:
        return func

    return decorator
