"""Transaction client."""

import functools
import typing
import urllib.parse

from genshin import paginators, utility
from genshin.client import routes
from genshin.client.components import base
from genshin.models.genshin import transaction as models

__all__ = ["TransactionClient"]


class TransactionClient(base.BaseClient):
    """Transaction component."""

    async def request_transaction(
        self,
        endpoint: str,
        *,
        method: str = "GET",
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the transaction log endpoint."""
        pass

    async def _get_transaction_page(
        self,
        end_id: int,
        kind: str,
        *,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
    ) -> typing.Sequence[models.BaseTransaction]:
        """Get a single page of transactions."""
        pass

    def transaction_log(
        self,
        kind: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        *,
        limit: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
        authkey: typing.Optional[str] = None,
        end_id: int = 0,
    ) -> paginators.Paginator[models.BaseTransaction]:
        """Get the transaction log of a user."""
        pass
