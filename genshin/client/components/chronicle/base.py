"""Base battle chronicle component."""

import asyncio
import dataclasses
import typing
import warnings

from genshin import errors, models, types, utility
from genshin.client import cache, routes
from genshin.client.components import base
from genshin.client.manager import managers
from genshin.constants import GAME_LANGS
from genshin.models import hoyolab as hoyolab_models
from genshin.utility import deprecation

__all__ = ["BaseBattleChronicleClient"]


@dataclasses.dataclass(unsafe_hash=True)
class HoyolabCacheKey(cache.CacheKey):
    endpoint: str
    hoyolab_id: int
    lang: str


@dataclasses.dataclass(unsafe_hash=True)
class ChronicleCacheKey(cache.CacheKey):
    def __str__(self) -> str:
        return "chronicle" + ":" + super().__str__()

    game: types.Game
    endpoint: str
    uid: int
    lang: str
    params: tuple[typing.Any, ...] = ()


class BaseBattleChronicleClient(base.BaseClient):
    """Base battle chronicle component."""

    async def request_game_record(
        self,
        endpoint: str,
        *,
        lang: typing.Optional[str] = None,
        region: typing.Optional[types.Region] = None,
        game: typing.Optional[types.Game] = None,
        custom_route: typing.Optional[typing.Union[routes.Route, routes.InternationalRoute]] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the game record endpoint."""
        pass

    async def get_record_cards(
        self, hoyolab_id: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> list[models.hoyolab.RecordCard]:
        """Get a user's record cards."""
        pass

    @deprecation.deprecated("get_record_cards")
    async def get_record_card(
        self, hoyolab_id: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> models.hoyolab.RecordCard:
        """Get a user's record card."""
        pass

    @managers.no_multi
    async def update_settings(
        self,
        setting: types.IDOr[hoyolab_models.RecordCardSetting],
        on: bool,
        *,
        game: typing.Optional[types.Game] = None,
    ) -> None:
        """Update user settings.

        Setting IDs:
            1: Show your Battle Chronicle on your profile.
            2: Show your Character Details in the Battle Chronicle.
            3: Enable your Real-Time Notes. (only for Genshin Impact)
        """
        pass

    @deprecation.deprecated("update_settings")
    async def set_visibility(self, public: bool, *, game: typing.Optional[types.Game] = None) -> None:
        """Set your data to public or private."""
        pass
