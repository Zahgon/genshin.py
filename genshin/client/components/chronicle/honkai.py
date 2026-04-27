"""Honkai battle chronicle component."""

import asyncio
import typing

from genshin import errors, types
from genshin.models.honkai import chronicle as models

from . import base

__all__ = ["HonkaiBattleChronicleClient"]


class HonkaiBattleChronicleClient(base.BaseBattleChronicleClient):
    """Honkai battle chronicle component."""

    async def _request_honkai_record(
        self,
        endpoint: str,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
        cache: bool = False,
    ) -> typing.Mapping[str, typing.Any]:
        """Get an arbitrary honkai object."""
        pass

    async def get_honkai_user(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.HonkaiUserStats:
        """Get honkai user stats."""
        pass

    async def get_honkai_battlesuits(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.FullBattlesuit]:
        """Get honkai battlesuits."""
        pass

    async def get_honkai_old_abyss(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.OldAbyss]:
        """Get honkai old abyss.

        Only for level > 80.
        """
        pass

    async def get_honkai_superstring_abyss(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.SuperstringAbyss]:
        """Get honkai superstring abyss.

        Only for level <= 80.
        """
        pass

    async def get_honkai_abyss(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[typing.Union[models.SuperstringAbyss, models.OldAbyss]]:
        """Get honkai abyss."""
        pass

    async def get_honkai_elysian_realm(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.ElysianRealm]:
        """Get honkai elysian realm."""
        pass

    async def get_honkai_memorial_arena(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.MemorialArena]:
        """Get honkai memorial arena."""
        pass

    @typing.overload
    async def get_honkai_notes(
        self, uid: int, *, lang: typing.Optional[str] = ..., return_raw_data: typing.Literal[False] = ...
    ) -> models.HonkaiNotes: ...
    @typing.overload
    async def get_honkai_notes(
        self, uid: int, *, lang: typing.Optional[str] = ..., return_raw_data: typing.Literal[True] = ...
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_honkai_notes(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
        return_raw_data: bool = False,
    ) -> typing.Union[models.HonkaiNotes, typing.Mapping[str, typing.Any]]:
        """Get honkai memorial arena."""
        pass

    async def get_full_honkai_user(
        self,
        uid: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.FullHonkaiUserStats:
        """Get a full honkai user."""
        pass

    get_old_abyss = get_honkai_old_abyss
    get_superstring_abyss = get_honkai_superstring_abyss
    get_elysian_realm = get_honkai_elysian_realm
    get_memorial_arena = get_honkai_memorial_arena
