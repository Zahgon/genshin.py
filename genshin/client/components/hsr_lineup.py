import typing

import aiohttp.typedefs

from genshin import types
from genshin.client import routes
from genshin.client.components import base
from genshin.constants import GAME_LANGS
from genshin.models.starrail import rpgsimulator as models
from genshin.utility import ds
from genshin.utility.uid import recognize_server

__all__ = ("HSRLineupClient",)

LineupGameMode = typing.Union[models.StarRailGameModeType, typing.Literal["Chasm", "Story", "Boss"]]


class HSRLineupClient(base.BaseClient):
    """HSR lineup simulator client."""

    async def _request(
        self,
        endpoint: str,
        *,
        lang: typing.Optional[str] = None,
        region: typing.Optional[types.Region] = None,
        method: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        data: typing.Any = None,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request any hoyolab endpoint."""
        pass

    async def get_starrail_lineup_game_modes(
        self, *, lang: typing.Optional[str] = None
    ) -> list[models.StarRailGameMode]:
        """Get the available game modes for the HSR lineup simulator."""
        pass

    def get_starrail_lineup_floor(
        self,
        game_modes: typing.Sequence[models.StarRailGameMode],
        *,
        type: LineupGameMode,
        floor: int,
    ) -> typing.Optional[models.StarRailGameModeFloor]:
        """Get a specific floor from the game modes."""
        pass

    @typing.overload
    async def get_starrail_lineups(
        self,
        *,
        tag_id: int,
        group_id: int,
        type: typing.Union[typing.Literal[models.StarRailGameModeType.MOC], typing.Literal["Chasm"]],
        next_page_token: typing.Optional[str] = ...,
        order: typing.Literal["Hot", "Match", "CreatedTime"] = ...,
        lang: typing.Optional[str] = ...,
    ) -> models.StarRailLineupResponse: ...
    @typing.overload
    async def get_starrail_lineups(
        self,
        *,
        tag_id: int,
        group_id: int,
        type: typing.Union[typing.Literal[models.StarRailGameModeType.PURE_FICTION], typing.Literal["Story"]],
        next_page_token: typing.Optional[str] = ...,
        order: typing.Literal["Hot", "Match", "CreatedTime"] = ...,
        lang: typing.Optional[str] = ...,
    ) -> models.PureFictionLineupResponse: ...
    @typing.overload
    async def get_starrail_lineups(
        self,
        *,
        tag_id: int,
        group_id: int,
        type: typing.Union[typing.Literal[models.StarRailGameModeType.APC_SHADOW], typing.Literal["Boss"]],
        next_page_token: typing.Optional[str] = ...,
        order: typing.Literal["Hot", "Match", "CreatedTime"] = ...,
        lang: typing.Optional[str] = ...,
    ) -> models.APCShadowLineupResponse: ...
    async def get_starrail_lineups(
        self,
        *,
        tag_id: int,
        group_id: int,
        type: LineupGameMode,
        next_page_token: typing.Optional[str] = None,
        order: typing.Literal["Hot", "Match", "CreatedTime"] = "Match",
        lang: typing.Optional[str] = None,
    ) -> typing.Union[models.StarRailLineupResponse, models.PureFictionLineupResponse, models.APCShadowLineupResponse]:
        """Get the available lineups for the HSR lineup simulator."""
        pass

    @typing.overload
    async def get_starrail_lineup_schedules(
        self,
        type: typing.Union[typing.Literal[models.StarRailGameModeType.MOC], typing.Literal["Chasm"]],
        *,
        lang: typing.Optional[str] = ...,
    ) -> list[models.MOCSchedule]: ...
    @typing.overload
    async def get_starrail_lineup_schedules(
        self,
        type: typing.Union[typing.Literal[models.StarRailGameModeType.PURE_FICTION], typing.Literal["Story"]],
        *,
        lang: typing.Optional[str] = ...,
    ) -> list[models.PureFictionSchedule]: ...
    @typing.overload
    async def get_starrail_lineup_schedules(
        self,
        type: typing.Union[typing.Literal[models.StarRailGameModeType.APC_SHADOW], typing.Literal["Boss"]],
        *,
        lang: typing.Optional[str] = ...,
    ) -> list[models.APCShadowSchedule]: ...
    async def get_starrail_lineup_schedules(
        self, type: LineupGameMode, *, lang: typing.Optional[str] = None
    ) -> typing.Union[list[models.MOCSchedule], list[models.PureFictionSchedule], list[models.APCShadowSchedule]]:
        """Get the schedule for the HSR lineup simulator."""
        pass
