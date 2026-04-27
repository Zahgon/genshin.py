"""Genshin battle chronicle component."""

import asyncio
import functools
import typing
import warnings

from genshin import errors, paginators, types, utility
from genshin.models.genshin import character as character_models
from genshin.models.genshin import chronicle as models

from . import base

__all__ = ["GenshinBattleChronicleClient"]


class GenshinBattleChronicleClient(base.BaseBattleChronicleClient):
    """Genshin battle chronicle component."""

    async def _request_genshin_record(
        self,
        endpoint: str,
        uid: typing.Optional[int] = None,
        *,
        method: str = "GET",
        lang: typing.Optional[str] = None,
        payload: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        cache: bool = False,
    ) -> typing.Mapping[str, typing.Any]:
        """Get an arbitrary genshin object."""
        pass

    async def get_partial_genshin_user(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.PartialGenshinUserStats:
        """Get partial genshin user without character equipment."""
        pass

    async def get_genshin_characters(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.Character]:
        """Get genshin user characters."""
        pass

    @typing.overload
    async def get_genshin_detailed_characters(
        self,
        uid: typing.Optional[int] = ...,
        *,
        characters: typing.Optional[typing.Sequence[int]] = ...,
        lang: typing.Optional[str] = ...,
        return_raw_data: typing.Literal[False] = ...,
    ) -> models.GenshinDetailCharacters: ...
    @typing.overload
    async def get_genshin_detailed_characters(
        self,
        uid: typing.Optional[int] = ...,
        *,
        characters: typing.Optional[typing.Sequence[int]] = ...,
        lang: typing.Optional[str] = ...,
        return_raw_data: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_genshin_detailed_characters(
        self,
        uid: typing.Optional[int] = None,
        *,
        characters: typing.Optional[typing.Sequence[int]] = None,
        lang: typing.Optional[str] = None,
        return_raw_data: bool = False,
    ) -> typing.Union[models.GenshinDetailCharacters, typing.Mapping[str, typing.Any]]:
        """Return a list of genshin characters with full details."""
        pass

    async def get_genshin_user(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.GenshinUserStats:
        """Get genshin user."""
        pass

    @typing.overload
    async def get_genshin_spiral_abyss(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> models.SpiralAbyss: ...
    @typing.overload
    async def get_genshin_spiral_abyss(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_genshin_spiral_abyss(
        self,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.SpiralAbyss, typing.Mapping[str, typing.Any]]:
        """Get genshin spiral abyss runs."""
        pass

    @typing.overload
    async def get_imaginarium_theater(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        need_detail: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> models.ImgTheater: ...
    @typing.overload
    async def get_imaginarium_theater(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        need_detail: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_imaginarium_theater(
        self,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        need_detail: bool = True,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.ImgTheater, typing.Mapping[str, typing.Any]]:
        """Get Genshin Impact imaginarium theater runs."""
        pass

    @typing.overload
    async def get_genshin_notes(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        autoauth: bool = ...,
        return_raw_data: typing.Literal[False] = ...,
    ) -> models.Notes: ...
    @typing.overload
    async def get_genshin_notes(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        autoauth: bool = ...,
        return_raw_data: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_genshin_notes(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
        autoauth: bool = True,
        return_raw_data: bool = False,
    ) -> typing.Union[models.Notes, typing.Mapping[str, typing.Any]]:
        """Get genshin real-time notes."""
        pass

    async def get_genshin_activities(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> models.Activities:
        """Get genshin activities."""
        pass

    async def get_genshin_tcg_preview(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> models.TCGPreview:
        """Get genshin tcg."""
        pass

    async def _get_genshin_tcg_page(
        self,
        page: int,
        *,
        uid: typing.Optional[int] = None,
        characters: bool = True,
        action: bool = True,
        limit: int = 32,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.TCGBaseCard]:
        """Get genshin tcg page."""
        pass

    def genshin_tcg(
        self,
        uid: typing.Optional[int] = None,
        *,
        limit: typing.Optional[int] = None,
        characters: bool = True,
        action: bool = True,
        page_size: int = 32,
        lang: typing.Optional[str] = None,
    ) -> paginators.PagedPaginator[models.TCGBaseCard]:
        """Get genshin tcg cards."""
        pass

    async def get_full_genshin_user(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.FullGenshinUserStats:
        """Get a genshin user with all their possible data."""
        pass

    async def set_top_genshin_characters(
        self,
        characters: typing.Sequence[types.IDOr[character_models.BaseCharacter]],
        *,
        uid: typing.Optional[int] = None,
    ) -> None:
        """Set the top 8 visible genshin characters for the current user."""
        pass

    async def get_genshin_event_calendar(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> models.GenshinEventCalendar:
        """Get Genshin event calendar."""
        pass

    async def get_envisaged_echoes(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> typing.Sequence[models.EnvisagedEchoCharacter]:
        """Get Genshin Envisaged Echo characters information."""
        pass

    @typing.overload
    async def get_stygian_onslaught(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
        need_detail: bool = ...,
    ) -> list[models.HardChallenge]: ...
    @typing.overload
    async def get_stygian_onslaught(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
        need_detail: bool = ...,
    ) -> list[typing.Mapping[str, typing.Any]]: ...
    async def get_stygian_onslaught(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
        raw: bool = False,
        need_detail: bool = True,
    ) -> typing.Union[list[models.HardChallenge], list[typing.Mapping[str, typing.Any]]]:
        """Get Stygian Onslaught data."""
        pass

    get_spiral_abyss = get_genshin_spiral_abyss
    get_notes = get_genshin_notes
    get_activities = get_genshin_activities
