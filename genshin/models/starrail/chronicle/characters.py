"""Starrail chronicle character."""

import typing
from collections.abc import Mapping, Sequence

import pydantic

from genshin.models.model import APIModel

from .. import character

__all__ = [
    "ModifyRelicProperty",
    "RecommendProperty",
    "StarRailDetailCharacterResponse",
    "StarRailSimpleCharacterResponse",
]


class RecommendProperty(APIModel):
    """Character recommended and preferred properties."""

    recommend_relic_properties: typing.Sequence[int]
    custom_relic_properties: typing.Sequence[int]
    is_custom_property_valid: bool


class ModifyRelicProperty(APIModel):
    """Modify relic property."""

    property_type: int
    modify_property_type: int


class StarRailSimpleCharacterResponse(APIModel):
    """HSR characters endpoint response model for when viewed by other players."""

    avatar_list: Sequence[character.StarRailSimpleCharacter]
    equip_wiki: Mapping[str, str]
    relic_wiki: Mapping[str, str]
    property_info: Mapping[str, character.PropertyInfo]
    recommend_property: Mapping[str, RecommendProperty]
    relic_properties: Sequence[ModifyRelicProperty]

    @pydantic.model_validator(mode="before")
    def __fill_additional_fields(cls, values: Mapping[str, typing.Any]) -> Mapping[str, typing.Any]:
        """Fill additional fields for convenience."""
        pass


class StarRailDetailCharacterResponse(StarRailSimpleCharacterResponse):
    """HSR characters endpoint response model for when viewed by the user."""

    avatar_list: Sequence[character.StarRailDetailCharacter]
