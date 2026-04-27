"""Genshin wish models."""

import enum
import json
import typing
import unicodedata

import pydantic

from genshin.models.model import Aliased, APIModel, Unique

__all__ = [
    "ArtifactPreview",
    "CharacterPreview",
    "EnemyPreview",
    "WeaponPreview",
    "WikiPage",
    "WikiPageType",
]


class WikiPageType(enum.IntEnum):
    """Wiki page types."""

    UNKNOWN = 0
    CHARACTER = 2
    WEAPON = 4
    ARTIFACT = 5
    ENEMY = 7


class BaseWikiPreview(APIModel, Unique):
    """Base wiki preview."""

    id: int = Aliased("entry_page_id")
    icon: str = Aliased("icon_url")
    name: str

    @pydantic.model_validator(mode="before")
    def __unpack_filter_values(cls, values: dict[str, typing.Any]) -> dict[str, typing.Any]:
        pass

    @pydantic.model_validator(mode="before")
    def __flatten_display_field(cls, values: dict[str, typing.Any]) -> dict[str, typing.Any]:
        pass


class CharacterPreview(BaseWikiPreview):
    """Character wiki preview."""

    bonus_attribute: str = Aliased("", "property")
    rarity: int
    region: str = ""
    element: str = Aliased("vision", "")
    weapon: str

    @pydantic.field_validator("rarity", mode="before")
    def __extract_rarity(cls, value: typing.Union[int, str]) -> int:
        pass


class WeaponPreview(BaseWikiPreview):
    """Weapon wiki preview."""

    bonus_attribute: str = Aliased("property")
    rarity: int
    type: str

    @pydantic.field_validator("rarity", mode="before")
    def __extract_rarity(cls, value: typing.Union[int, str]) -> int:
        pass


class ArtifactPreview(BaseWikiPreview):
    """Artifact wiki preview."""

    effect: str

    circlet_icon: str = Aliased("circlet_of_logos_icon_url")
    flower_icon: str = Aliased("flower_of_life_icon_url")
    goblet_icon: str = Aliased("goblet_of_eonothem_icon_url")
    plume_icon: str = Aliased("plume_of_death_icon_url")
    sands_icon: str = Aliased("sands_of_eon_icon_url")

    effects: typing.Mapping[int, str]

    @pydantic.model_validator(mode="before")
    def __group_effects(cls, values: dict[str, typing.Any]) -> dict[str, typing.Any]:
        pass


class EnemyPreview(BaseWikiPreview):
    """Enemy wiki preview."""

    drop_materials: typing.Sequence[str]

    @pydantic.field_validator("drop_materials", mode="before")
    def __parse_drop_materials(cls, value: typing.Union[str, typing.Sequence[str]]) -> typing.Sequence[str]:
        pass


_ENTRY_PAGE_MODELS: typing.Mapping[WikiPageType, type[BaseWikiPreview]] = {
    WikiPageType.CHARACTER: CharacterPreview,
    WikiPageType.WEAPON: WeaponPreview,
    WikiPageType.ARTIFACT: ArtifactPreview,
    WikiPageType.ENEMY: EnemyPreview,
}


class WikiPage(APIModel):
    """Wiki page."""

    id: int
    page_type: WikiPageType = Aliased("menu_id")

    description: str = Aliased("desc")
    header: str = Aliased("header_img_url")
    icon: str = Aliased("icon_url")

    modules: typing.Mapping[str, typing.Mapping[str, typing.Any]]

    @pydantic.field_validator("modules", mode="before")
    def __format_modules(
        cls,
        value: typing.Union[list[dict[str, typing.Any]], dict[str, typing.Any]],
    ) -> dict[str, typing.Any]:
        pass
