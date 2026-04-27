"""StarRail battle chronicle component."""

import asyncio
import typing

from genshin import errors, types, utility
from genshin.models.starrail import chronicle as models

from . import base

__all__ = ["StarRailBattleChronicleClient"]


class StarRailBattleChronicleClient(base.BaseBattleChronicleClient):
    """StarRail battle chronicle component."""

    async def _request_starrail_record(
        self,
        endpoint: str,
        uid: typing.Optional[int] = None,
        *,
        method: str = "GET",
        lang: typing.Optional[str] = None,
        payload: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        cache: bool = False,
    ) -> typing.Mapping[str, typing.Any]:
        """Get an arbitrary starrail object."""
        pass

    @typing.overload
    async def get_starrail_notes(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        autoauth: bool = ...,
        return_raw_data: typing.Literal[False] = ...,
    ) -> models.StarRailNote: ...
    @typing.overload
    async def get_starrail_notes(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        autoauth: bool = ...,
        return_raw_data: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_starrail_notes(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
        autoauth: bool = True,
        return_raw_data: bool = False,
    ) -> typing.Union[models.StarRailNote, typing.Mapping[str, typing.Any]]:
        """Get starrail real-time notes."""
        pass

    async def get_starrail_user(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.StarRailUserStats:
        """Get starrail user."""
        pass

    @typing.overload
    async def get_starrail_characters(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        simple: typing.Literal[False] = ...,
    ) -> models.StarRailDetailCharacterResponse: ...

    @typing.overload
    async def get_starrail_characters(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        simple: typing.Literal[True] = ...,
    ) -> models.StarRailSimpleCharacterResponse: ...

    async def get_starrail_characters(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
        simple: bool = False,
    ) -> typing.Union[models.StarRailSimpleCharacterResponse, models.StarRailDetailCharacterResponse]:
        """Get starrail characters."""
        pass

    @typing.overload
    async def get_starrail_challenge(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> models.StarRailChallenge: ...
    @typing.overload
    async def get_starrail_challenge(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_starrail_challenge(
        self,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.StarRailChallenge, typing.Mapping[str, typing.Any]]:
        """Get starrail challenge runs."""
        pass

    async def get_starrail_rogue(
        self,
        uid: typing.Optional[int] = None,
        *,
        schedule_type: int = 3,
        lang: typing.Optional[str] = None,
    ) -> models.StarRailRogue:
        """Get starrail rogue runs."""
        pass

    @typing.overload
    async def get_starrail_pure_fiction(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> models.StarRailPureFiction: ...
    @typing.overload
    async def get_starrail_pure_fiction(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_starrail_pure_fiction(
        self,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.StarRailPureFiction, typing.Mapping[str, typing.Any]]:
        """Get starrail pure fiction runs."""
        pass

    @typing.overload
    async def get_starrail_apc_shadow(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> models.StarRailAPCShadow: ...
    @typing.overload
    async def get_starrail_apc_shadow(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_starrail_apc_shadow(
        self,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.StarRailAPCShadow, typing.Mapping[str, typing.Any]]:
        """Get starrail apocalyptic shadow runs."""
        pass

    async def get_starrail_event_calendar(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.HSREventCalendar:
        """Get HSR event calendar."""
        pass

    get_apocalyptic_shadow = get_starrail_apc_shadow
    """Alias for :meth:`get_starrail_apc_shadow`."""

    @typing.overload
    async def get_anomaly_arbitration(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> models.AnomalyArbitration: ...
    @typing.overload
    async def get_anomaly_arbitration(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_anomaly_arbitration(
        self,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.AnomalyArbitration, typing.Mapping[str, typing.Any]]:
        """Get starrail anomaly arbitration runs."""
        pass
