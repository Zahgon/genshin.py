"""Lineup component."""

import functools
import typing

import genshin.models.genshin as genshin_models
from genshin import paginators, types, utility
from genshin.client import cache, routes
from genshin.client.components import base
from genshin.client.manager import managers
from genshin.models.genshin import lineup as models

__all__ = ["LineupClient"]


class LineupClient(base.BaseClient):
    """Lineup component."""

    async def request_lineup(
        self,
        endpoint: str,
        *,
        method: str = "GET",
        lang: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the lineup endpoint."""
        pass

    async def get_lineup_fields(
        self, *, lang: typing.Optional[str] = None, use_cache: bool = True
    ) -> models.LineupFields:
        """Get configuration lineup fields."""
        pass

    async def get_lineup_scenarios(
        self,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.LineupScenarios:
        """Get lineup scenarios."""
        pass

    async def _get_lineup_page(
        self,
        token: str,
        *,
        limit: typing.Optional[int] = None,
        tag_id: typing.Optional[int] = None,
        roles: typing.Optional[typing.Sequence[int]] = None,
        order: typing.Optional[str] = None,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> tuple[str, typing.Sequence[models.LineupPreview]]:
        """Get a single page of lineups."""
        pass

    def get_lineups(
        self,
        scenario: typing.Optional[types.IDOr[models.LineupScenario]] = None,
        *,
        limit: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        newest: bool = False,
        match_characters: bool = False,
        characters: typing.Optional[typing.Sequence[types.IDOr[genshin_models.Character]]] = None,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> paginators.TokenPaginator[models.LineupPreview]:
        """Get lineups."""
        pass

    async def get_lineup_details(
        self,
        lineup: typing.Union[str, models.LineupPreview],
        *,
        lang: typing.Optional[str] = None,
    ) -> models.Lineup:
        """Get lineup with detailed characters."""
        pass

    @managers.no_multi
    async def get_user_lineups(
        self,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.LineupPreview]:
        """Get lineups of the currently logged-in user."""
        pass

    @managers.no_multi
    async def get_favorite_lineups(
        self,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.LineupPreview]:
        """Get favorited lineups of the currently logged-in user."""
        pass

    @managers.no_multi
    async def get_lineup_character_history(
        self,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.LineupCharacter]:
        """Get previous character builds of the currently logged-in user.."""
        pass
