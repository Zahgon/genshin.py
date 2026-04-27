"""Diary component."""

import datetime
import functools
import typing

from genshin import paginators, types, utility
from genshin.client import cache, routes
from genshin.client.components import base
from genshin.client.manager import managers
from genshin.constants import CN_TIMEZONE
from genshin.models.genshin import diary as models
from genshin.utility import deprecation

__all__ = ["DiaryClient"]


class DiaryCallback(typing.Protocol):
    """Callback which requires a diary page."""

    async def __call__(self, page: int, /) -> models.DiaryPage:
        """Return a diary page."""
        ...


class DiaryPaginator(paginators.PagedPaginator[models.DiaryAction]):
    """Paginator for diary."""

    _data: typing.Optional[models.DiaryPage]
    """Metadata of the paginator"""

    def __init__(self, getter: DiaryCallback, *, limit: typing.Optional[int] = None) -> None:
        self._get_page = getter
        self._data = None

        super().__init__(self._getter, limit=limit, page_size=100)

    async def _getter(self, page: int) -> typing.Sequence[models.DiaryAction]:
        pass

    @property
    def data(self) -> models.BaseDiary:
        """Get data bound to the diary.

        This requires at least one page to have been fetched.
        """
        pass


class StarRailDiaryCallback(typing.Protocol):
    """Callback which requires a diary page."""

    async def __call__(self, page: int, /) -> models.StarRailDiaryPage:
        """Return a diary page."""
        ...


class StarRailDiaryPaginator(paginators.PagedPaginator[models.StarRailDiaryAction]):
    """Paginator for diary."""

    _data: typing.Optional[models.StarRailDiaryPage]
    """Metadata of the paginator"""

    def __init__(self, getter: StarRailDiaryCallback, *, limit: typing.Optional[int] = None) -> None:
        self._get_page = getter
        self._data = None

        super().__init__(self._getter, limit=limit, page_size=100)

    async def _getter(self, page: int) -> typing.Sequence[models.StarRailDiaryAction]:
        pass

    @property
    def data(self) -> models.BaseDiary:
        """Get data bound to the diary.

        This requires at least one page to have been fetched.
        """
        pass


class DiaryClient(base.BaseClient):
    """Diary component."""

    @managers.no_multi
    async def request_ledger(
        self,
        uid: typing.Optional[int] = None,
        *,
        game: typing.Optional[types.Game] = None,
        detail: bool = False,
        month: typing.Union[int, str, None] = None,
        lang: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the ys ledger endpoint."""
        pass

    @deprecation.deprecated("get_genshin_diary")
    async def get_diary(
        self,
        uid: typing.Optional[int] = None,
        *,
        month: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> models.Diary:
        """Get a traveler's diary with earning details for the month."""
        pass

    async def get_genshin_diary(
        self,
        uid: typing.Optional[int] = None,
        *,
        month: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> models.Diary:
        """Get a traveler's diary with earning details for the month."""
        pass

    async def get_starrail_diary(
        self,
        uid: typing.Optional[int] = None,
        *,
        month: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> models.StarRailDiary:
        """Get a blazer's diary with earning details for the month."""
        pass

    async def _get_genshin_diary_page(
        self,
        page: int,
        *,
        uid: typing.Optional[int] = None,
        type: int = models.DiaryType.PRIMOGEMS,
        month: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> models.DiaryPage:
        pass

    @deprecation.deprecated("genshin_diary_log")
    def diary_log(
        self,
        uid: typing.Optional[int] = None,
        *,
        limit: typing.Optional[int] = None,
        type: int = models.DiaryType.PRIMOGEMS,
        month: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> DiaryPaginator:
        """Create a new daily reward paginator."""
        pass

    def genshin_diary_log(
        self,
        uid: typing.Optional[int] = None,
        *,
        limit: typing.Optional[int] = None,
        type: int = models.DiaryType.PRIMOGEMS,
        month: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> DiaryPaginator:
        """Create a new daily reward paginator."""
        pass

    async def _get_starrail_diary_page(
        self,
        page: int,
        *,
        uid: typing.Optional[int] = None,
        type: int = models.StarRailDiaryType.STELLARJADE,
        month: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
    ) -> models.StarRailDiaryPage:
        pass

    def starrail_diary_log(
        self,
        uid: typing.Optional[int] = None,
        *,
        limit: typing.Optional[int] = None,
        type: int = models.StarRailDiaryType.STELLARJADE,
        month: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
    ) -> StarRailDiaryPaginator:
        """Create a new daily reward paginator."""
        pass
