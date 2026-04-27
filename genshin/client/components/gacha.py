"""Wish component."""

import asyncio
import functools
import logging
import typing
import urllib.parse
import warnings

from pydantic import ValidationError

from genshin import paginators, types, utility
from genshin.client import cache as client_cache
from genshin.client import routes
from genshin.client.components import base
from genshin.models.genshin import gacha as models
from genshin.utility import deprecation

__all__ = ["WishClient"]

FATE_BANNER_TYPES = {models.StarRailBannerType.FATE_CHARACTER, models.StarRailBannerType.FATE_WEAPON}
MW_BANNER_TYPES = {
    models.MWBannerType.STANDARD,
    models.MWBannerType.EVENT,
}
LOGGER_ = logging.getLogger(__name__)


class WishClient(base.BaseClient):
    """Wish component."""

    async def request_gacha_info(
        self,
        endpoint: str,
        *,
        lang: typing.Optional[str] = None,
        game: typing.Optional[types.Game] = None,
        authkey: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        short_lang_code: bool = True,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the gacha info endpoint."""
        pass

    async def _get_gacha_page(
        self,
        end_id: int,
        banner_type: int,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
    ) -> tuple[typing.Sequence[typing.Any], int]:
        """Get a single page of wishes."""
        pass

    async def _get_wish_page(
        self,
        end_id: int,
        banner_type: models.GenshinBannerType,
        *,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
    ) -> typing.Sequence[models.Wish]:
        """Get a single page of wishes."""
        pass

    async def _get_mw_wish_page(
        self,
        end_id: int,
        banner_type: models.MWBannerType,
        *,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
    ) -> typing.Sequence[models.MWWish]:
        """Get a single page of Miliastra Wonderland wishes."""
        pass

    async def _get_warp_page(
        self,
        end_id: int,
        banner_type: models.StarRailBannerType,
        *,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
    ) -> typing.Sequence[models.Warp]:
        """Get a single page of warps."""
        pass

    async def _get_signal_page(
        self,
        end_id: int,
        banner_type: models.ZZZBannerType,
        *,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
    ) -> typing.Sequence[models.SignalSearch]:
        """Get a single page of signal searches."""
        pass

    def wish_history(
        self,
        banner_type: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
        end_id: int = 0,
    ) -> paginators.Paginator[models.Wish]:
        """Get the wish history of a user."""
        pass

    def mw_wish_history(
        self,
        banner_type: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
        end_id: int = 0,
    ) -> paginators.Paginator[models.MWWish]:
        """Get the Miliastra Wonderland wish history of a user."""
        pass

    def warp_history(
        self,
        banner_type: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
        end_id: int = 0,
    ) -> paginators.Paginator[models.Warp]:
        """Get the warp history of a user."""
        pass

    def signal_history(
        self,
        banner_type: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
        end_id: int = 0,
    ) -> paginators.Paginator[models.SignalSearch]:
        """Get the signal search history of a user."""
        pass

    @deprecation.deprecated("get_genshin_banner_names")
    async def get_banner_names(
        self,
        *,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
    ) -> typing.Mapping[int, str]:
        """Get a list of banner names."""
        pass

    async def get_genshin_banner_names(
        self,
        *,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
    ) -> typing.Mapping[int, str]:
        """Get a list of banner names."""
        pass

    async def _get_banner_details(
        self,
        banner_id: str,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
    ) -> models.BannerDetails:
        """Get details of a specific banner using its id."""
        pass

    @deprecation.deprecated("get_genshin_banner_ids")
    async def get_banner_ids(self) -> typing.Sequence[str]:
        """Get a list of banner ids.

        Uses the current cn banners.
        """
        pass

    async def get_genshin_banner_ids(self) -> typing.Sequence[str]:
        """Get a list of banner ids.

        Uses the current cn banners.
        """
        pass

    async def get_banner_details(
        self,
        banner_ids: typing.Optional[typing.Sequence[str]] = None,
        *,
        game: typing.Optional[types.Game] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.BannerDetails]:
        """Get all banner details at once in a batch."""
        pass

    @deprecation.deprecated("get_genshin_gacha_items")
    async def get_gacha_items(
        self,
        *,
        server: str = "os_asia",
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.GachaItem]:
        """Get the list of characters and weapons that can be gotten from the gacha."""
        pass

    async def get_genshin_gacha_items(
        self,
        *,
        server: str = "os_asia",
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.GachaItem]:
        """Get the list of characters and weapons that can be gotten from the gacha."""
        pass
