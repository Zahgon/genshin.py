"""StarRail battle chronicle component."""

import asyncio
import functools
import typing

from genshin import errors, paginators, types, utility
from genshin.client import routes
from genshin.models import zzz as models
from genshin.models.genshin import gacha as gacha_models

from . import base

__all__ = ("ZZZBattleChronicleClient",)


class ZZZBattleChronicleClient(base.BaseBattleChronicleClient):
    """ZZZ battle chronicle component."""

    async def _request_zzz_record(
        self,
        endpoint: str,
        uid: typing.Optional[int] = None,
        *,
        method: str = "GET",
        lang: typing.Optional[str] = None,
        payload: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        cache: bool = False,
        is_nap_ledger: bool = False,
        use_uid_in_payload: bool = False,
    ) -> typing.Mapping[str, typing.Any]:
        """Get an arbitrary ZZZ object."""
        pass

    @typing.overload
    async def get_zzz_notes(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        autoauth: bool = ...,
        return_raw_data: typing.Literal[False] = ...,
    ) -> models.ZZZNotes: ...
    @typing.overload
    async def get_zzz_notes(
        self,
        uid: typing.Optional[int] = ...,
        *,
        lang: typing.Optional[str] = ...,
        autoauth: bool = ...,
        return_raw_data: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_zzz_notes(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
        autoauth: bool = True,
        return_raw_data: bool = False,
    ) -> typing.Union[models.ZZZNotes, typing.Mapping[str, typing.Any]]:
        """Get ZZZ sticky notes (real-time notes)."""
        pass

    async def get_zzz_diary(
        self,
        uid: typing.Optional[int] = None,
        *,
        month: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
    ) -> models.ZZZDiary:
        """Get ZZZ inter-knot monthly earning data."""
        pass

    async def get_zzz_diary_detail(
        self,
        month: str,
        *,
        type: models.ZZZCurrencyType,
        page: int = 1,
        page_size: int = 20,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> models.ZZZDiaryDetail:
        """Get ZZZ inter-knot monthly earning data."""
        pass

    async def get_zzz_user(
        self,
        uid: typing.Optional[int] = None,
        *,
        lang: typing.Optional[str] = None,
    ) -> models.ZZZUserStats:
        """Get ZZZ user stats."""
        pass

    async def get_zzz_agents(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> typing.Sequence[models.ZZZPartialAgent]:
        """Get all owned ZZZ characters (only brief info)."""
        pass

    async def get_bangboos(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> typing.Sequence[models.ZZZBaseBangboo]:
        """Get all owned ZZZ bangboos."""
        pass

    @typing.overload
    async def get_zzz_agent_info(
        self,
        character_id: int,
        *,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> models.ZZZFullAgent: ...
    @typing.overload
    async def get_zzz_agent_info(
        self,
        character_id: typing.Sequence[int],
        *,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.ZZZFullAgent]: ...
    async def get_zzz_agent_info(
        self,
        character_id: typing.Union[int, typing.Sequence[int]],
        *,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Union[models.ZZZFullAgent, typing.Sequence[models.ZZZFullAgent]]:
        """Get a ZZZ character's detailed info."""
        pass

    @typing.overload
    async def get_shiyu_defense(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> typing.Union[models.ShiyuDefenseV1, models.ShiyuDefenseV2]: ...
    @typing.overload
    async def get_shiyu_defense(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_shiyu_defense(
        self,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.ShiyuDefenseV1, models.ShiyuDefenseV2, typing.Mapping[str, typing.Any]]:
        """Get ZZZ Shiyu defense stats."""
        pass

    @typing.overload
    async def get_deadly_assault(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> models.DeadlyAssault: ...
    @typing.overload
    async def get_deadly_assault(
        self,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_deadly_assault(
        self,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.DeadlyAssault, typing.Mapping[str, typing.Any]]:
        """Get ZZZ Shiyu defense stats."""
        pass

    async def get_lost_void_summary(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> models.LostVoidSummary:
        """Get ZZZ Lost Void summary."""
        pass

    async def get_threshold_simulation_brief(
        self, uid: typing.Optional[int] = None, *, previous: bool = False, lang: typing.Optional[str] = None
    ) -> models.ThresholdSimulationInfo:
        """Get ZZZ Threshold Simulation brief info."""
        pass

    @typing.overload
    async def get_threshold_simulation(
        self,
        id: typing.Optional[int] = ...,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[False] = ...,
    ) -> models.ThresholdSimulation: ...
    @typing.overload
    async def get_threshold_simulation(
        self,
        id: typing.Optional[int] = ...,
        uid: typing.Optional[int] = ...,
        *,
        previous: bool = ...,
        lang: typing.Optional[str] = ...,
        raw: typing.Literal[True] = ...,
    ) -> typing.Mapping[str, typing.Any]: ...
    async def get_threshold_simulation(
        self,
        id: typing.Optional[int] = None,
        uid: typing.Optional[int] = None,
        *,
        previous: bool = False,
        lang: typing.Optional[str] = None,
        raw: bool = False,
    ) -> typing.Union[models.ThresholdSimulation, typing.Mapping[str, typing.Any]]:
        """Get ZZZ Threshold Simulation stats.

        If no ID is given, the latest run will be fetched.
        """
        pass

    async def _get_chronicle_signal_page(
        self,
        end_id: int,
        banner_type: gacha_models.ZZZBannerType,
        *,
        lang: typing.Optional[str] = None,
        uid: typing.Optional[int] = None,
    ) -> typing.Sequence[gacha_models.SignalSearch]:
        """Get a single page of battle chronicle signal searches."""
        pass

    def chronicle_signal_history(
        self,
        banner_type: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
        uid: typing.Optional[int] = None,
        end_id: int = 0,
    ) -> paginators.Paginator[gacha_models.SignalSearch]:
        """Get the signal search history of a user."""
        pass

    async def get_zzz_event_calendar(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> typing.Sequence[models.ZZZEvent]:
        """Get ZZZ event calendar."""
        pass

    async def get_zzz_gacha_calendar(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> models.ZZZGachaCalendar:
        """Get ZZZ gacha calendar."""
        pass

    async def get_zzz_gacha_info(
        self, uid: typing.Optional[int] = None, *, lang: typing.Optional[str] = None
    ) -> models.ZZZGachaInfo:
        """Get ZZZ gacha info."""
        pass
