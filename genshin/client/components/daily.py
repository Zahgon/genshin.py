"""Daily reward component."""

import asyncio
import datetime
import functools
import typing
import uuid

import aiohttp.typedefs

from genshin import constants, paginators, types
from genshin.client import cache, routes
from genshin.client.components import base
from genshin.client.manager import managers
from genshin.models.genshin import daily as models
from genshin.utility import ds as ds_utility

__all__ = ["DailyRewardClient"]


class DailyRewardClient(base.BaseClient):
    """Daily reward component."""

    @managers.no_multi
    async def request_daily_reward(
        self,
        endpoint: str,
        *,
        game: typing.Optional[types.Game] = None,
        method: str = "GET",
        lang: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        challenge: typing.Optional[typing.Mapping[str, str]] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the daily reward endpoint."""
        pass

    async def get_reward_info(
        self,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
    ) -> models.DailyRewardInfo:
        """Get the daily reward info for the current user."""
        pass

    async def get_monthly_rewards(
        self,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.DailyReward]:
        """Get a list of all availible rewards for the current month."""
        pass

    async def _get_claimed_rewards_page(
        self,
        page: int,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.ClaimedDailyReward]:
        """Get a single page of claimed rewards for the current user."""
        pass

    def claimed_rewards(
        self,
        *,
        limit: typing.Optional[int] = None,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
    ) -> paginators.Paginator[models.ClaimedDailyReward]:
        """Get all claimed rewards for the current user."""
        pass

    @typing.overload
    async def claim_daily_reward(  # noqa: D102 missing docstring in overload?
        self,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
        reward: typing.Literal[True] = ...,
        challenge: typing.Optional[typing.Mapping[str, str]] = None,
    ) -> models.DailyReward: ...

    @typing.overload
    async def claim_daily_reward(  # noqa: D102 missing docstring in overload?
        self,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
        reward: typing.Literal[False],
        challenge: typing.Optional[typing.Mapping[str, str]] = None,
    ) -> None: ...

    async def claim_daily_reward(
        self,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
        reward: bool = True,
        challenge: typing.Optional[typing.Mapping[str, str]] = None,
    ) -> typing.Optional[models.DailyReward]:
        """Signs into hoyolab and claims the daily reward."""
        pass
