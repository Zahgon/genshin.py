"""Wiki component."""

import typing

from genshin import types
from genshin.client import cache, routes
from genshin.client.components import base
from genshin.models.genshin import wiki as models

__all__ = ["WikiClient"]


class WikiClient(base.BaseClient):
    """Wiki component."""

    async def request_wiki(
        self,
        endpoint: str,
        *,
        lang: typing.Optional[str] = None,
        headers: typing.Optional[typing.Mapping[str, str]] = None,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the wiki endpoint."""
        pass

    @typing.overload
    async def get_wiki_previews(  # noqa: D102 missing docstring in overload?
        self,
        menu: typing.Literal[models.WikiPageType.CHARACTER],
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.CharacterPreview]: ...

    @typing.overload
    async def get_wiki_previews(  # noqa: D102 missing docstring in overload?
        self,
        menu: typing.Literal[models.WikiPageType.WEAPON],
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.WeaponPreview]: ...

    @typing.overload
    async def get_wiki_previews(  # noqa: D102 missing docstring in overload?
        self,
        menu: typing.Literal[models.WikiPageType.ARTIFACT],
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.ArtifactPreview]: ...

    @typing.overload
    async def get_wiki_previews(  # noqa: D102 missing docstring in overload?
        self,
        menu: typing.Literal[models.WikiPageType.ENEMY],
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.EnemyPreview]: ...

    @typing.overload
    async def get_wiki_previews(  # noqa: D102 missing docstring in overload?
        self,
        menu: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.BaseWikiPreview]: ...

    async def get_wiki_previews(
        self,
        menu: int,
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.BaseWikiPreview]:
        """Get a list of wiki previews."""
        pass

    async def get_wiki_page(
        self,
        id: types.IDOr[models.BaseWikiPreview],
        *,
        lang: typing.Optional[str] = None,
    ) -> models.WikiPage:
        """Get a wiki page."""
        pass

    async def get_wiki_pages(
        self,
        ids: typing.Collection[types.IDOr[models.BaseWikiPreview]],
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.WikiPage]:
        """Get multiple wiki pages without modules."""
        pass
