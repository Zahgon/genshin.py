"""Hoyolab component."""

import asyncio
import json
import time
import typing
import uuid
import warnings

import yarl

from genshin import constants, types, utility
from genshin.client import cache as client_cache
from genshin.client import routes
from genshin.client.components import base
from genshin.client.manager import managers
from genshin.models import hoyolab as models

__all__ = ["HoyolabClient"]


class HoyolabClient(base.BaseClient):
    """Hoyolab component."""

    async def _get_server_region(self, uid: int, game: types.Game) -> str:
        """Fetch the server region of an account from the API."""
        pass

    async def _request_announcements(
        self,
        game: types.Game,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.Announcement]:
        """Get a list of game announcements."""
        pass

    async def _request_mimo(
        self,
        endpoint: str,
        *,
        method: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        data: typing.Any = None,
    ) -> typing.Any:
        pass

    async def search_users(
        self,
        keyword: str,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.PartialHoyolabUser]:
        """Search hoyolab users."""
        pass

    async def get_hoyolab_user(
        self,
        hoyolab_id: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.FullHoyolabUser:
        """Get a hoyolab user."""
        pass

    async def get_recommended_users(self, *, limit: int = 200) -> typing.Sequence[models.PartialHoyolabUser]:
        """Get a list of recommended active users."""
        pass

    async def get_genshin_announcements(
        self,
        *,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.Announcement]:
        """Get a list of Genshin Impact announcements."""
        pass

    async def get_zzz_announcements(
        self,
        *,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.Announcement]:
        """Get a list of Zenless Zone Zero announcements."""
        pass

    async def get_starrail_announcements(
        self,
        *,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.Announcement]:
        """Get a list of Star Rail announcements."""
        pass

    @managers.requires_cookie_token
    async def redeem_code(
        self,
        code: str,
        uid: typing.Optional[int] = None,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
    ) -> None:
        """Redeems a gift code for the current user."""
        pass

    @managers.no_multi
    async def check_in_community(self) -> None:
        """Check in to the hoyolab community and claim your daily 5 community exp."""
        raise RuntimeError("This API is deprecated.")

    @base.region_specific(types.Region.OVERSEAS)
    async def fetch_mi18n(
        self, url: typing.Union[str, yarl.URL], filename: str, *, lang: typing.Optional[str] = None
    ) -> typing.Mapping[str, str]:
        """Fetch a mi18n file."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def get_mimo_games(self, *, lang: typing.Optional[str] = None) -> typing.Sequence[models.MimoGame]:
        """Get a list of Traveling Mimo games."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def _get_mimo_game_data(
        self, game: typing.Union[typing.Literal["hoyolab"], types.Game]
    ) -> typing.Tuple[int, int]:
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def _parse_mimo_args(
        self,
        game_id: typing.Optional[int] = None,
        version_id: typing.Optional[int] = None,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
    ) -> typing.Tuple[int, int]:
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def get_mimo_tasks(
        self,
        *,
        game_id: typing.Optional[int] = None,
        version_id: typing.Optional[int] = None,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.MimoTask]:
        """Get a list of Traveling Mimo missions (tasks)."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def claim_mimo_task_reward(
        self,
        task_id: int,
        *,
        game_id: typing.Optional[int] = None,
        version_id: typing.Optional[int] = None,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
        lang: typing.Optional[str] = None,
    ) -> None:
        """Claim a Traveling Mimo mission (task) reward."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def finish_mimo_task(
        self,
        task_id: int,
        *,
        game_id: typing.Optional[int] = None,
        version_id: typing.Optional[int] = None,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
        lang: typing.Optional[str] = None,
    ) -> None:
        """Finish a Traveling Mimo mission (task) reward."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def get_mimo_shop_items(
        self,
        *,
        game_id: typing.Optional[int] = None,
        version_id: typing.Optional[int] = None,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.MimoShopItem]:
        """Get a list of Traveling Mimo shop items."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def buy_mimo_shop_item(
        self,
        item_id: int,
        *,
        game_id: typing.Optional[int] = None,
        version_id: typing.Optional[int] = None,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
        lang: typing.Optional[str] = None,
    ) -> str:
        """Buy an item from the Traveling Mimo shop and return a gift code to redeem it."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def get_mimo_point_count(
        self,
        *,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
    ) -> int:
        """Get the current Traveling Mimo point count."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def get_mimo_lottery_info(
        self,
        *,
        game_id: typing.Optional[int] = None,
        version_id: typing.Optional[int] = None,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
        lang: typing.Optional[str] = None,
    ) -> models.MimoLotteryInfo:
        """Get Traveling Mimo lottery info."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def draw_mimo_lottery(
        self,
        *,
        game_id: typing.Optional[int] = None,
        version_id: typing.Optional[int] = None,
        game: typing.Optional[typing.Union[typing.Literal["hoyolab"], types.Game]] = None,
        lang: typing.Optional[str] = None,
    ) -> models.MimoLotteryResult:
        """Draw a Traveling Mimo lottery."""
        pass

    async def reply_to_post(self, content: str, *, post_id: int) -> int:
        """Reply to a community post."""
        pass

    async def delete_reply(self, *, reply_id: int, post_id: int) -> None:
        """Delete a reply."""
        pass

    async def _request_join(self, topic_id: int, *, is_cancel: bool) -> None:
        pass

    async def join_topic(self, topic_id: int) -> None:
        """Join a topic."""
        pass

    async def leave_topic(self, topic_id: int) -> None:
        """Leave a topic."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def get_web_events(
        self,
        game: typing.Optional[types.Game] = None,
        *,
        size: int = 15,
        offset: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> list[models.WebEvent]:
        """Get a list of web events."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def get_accompany_characters(
        self, *, lang: typing.Optional[str] = None
    ) -> typing.Sequence[models.AccompanyCharacterGame]:
        """Get a list of accompany characters, this endpoint doesn't require cookies."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def accompany_character(self, *, role_id: int, topic_id: int) -> models.AccompanyResult:
        """Accompany a character, role_id and topic_id can be found by calling get_accompany_characters."""
        pass
