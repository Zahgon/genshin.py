"""Teapot component."""

import functools
import typing

from genshin import paginators, utility
from genshin.client import routes
from genshin.client.components import base
from genshin.models.genshin import teapot as models

__all__ = ["TeapotClient"]


class TeapotClient(base.BaseClient):
    """teapot component."""

    async def request_teapot(
        self,
        endpoint: str,
        *,
        method: str = "GET",
        lang: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the teapot endpoint."""
        pass

    async def _get_teapot_replica_page(
        self,
        page: int,
        *,
        zip_type: int = 1,
        block_id: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        limit: int = 20,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.TeapotReplica]:
        """Get a teapot replica page."""
        pass

    def teapot_replicas(
        self,
        *,
        limit: typing.Optional[int] = None,
        zip_type: int = 1,
        block_id: typing.Optional[str] = None,
        module_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        uid: typing.Optional[int] = None,
        version: typing.Optional[str] = None,
        page_size: int = 20,
        lang: typing.Optional[str] = None,
    ) -> paginators.PagedPaginator[models.TeapotReplica]:
        """Get a teapot replica paginator."""
        pass
