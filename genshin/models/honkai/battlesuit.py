"""Honkai battlesuit model."""

import logging
import re

import pydantic

from genshin.models.model import Aliased, APIModel, Unique

from .constants import BATTLESUIT_IDENTIFIERS

__all__ = ["Battlesuit"]

_LOGGER = logging.getLogger(__name__)

BATTLESUIT_TYPES = {
    "ShengWu": "BIO",
    "JiXie": "MECH",
    "YiNeng": "PSY",
    "LiangZi": "QUA",
    "XuShu": "IMG",
    "Xingchen": "SD",
}
ICON_BASE = "https://upload-os-bbs.mihoyo.com/game_record/honkai3rd/global/SpriteOutput/"


class Battlesuit(APIModel, Unique):
    """Represents a battlesuit without equipment or level."""

    id: int
    name: str
    rarity: int = Aliased("star")
    closeup_icon_background: str = Aliased("avatar_background_path")
    tall_icon: str = Aliased("figure_path")
    banner_art: str = Aliased("image_path")

    @pydantic.field_validator("tall_icon")
    def __autocomplete_figpath(cls, tall_icon: str, info: pydantic.ValidationInfo) -> str:
        """figure_path is empty for gamemode endpoints, and cannot be inferred from other fields."""
        pass

    @property
    def character(self) -> str:
        pass

    @property
    def rank(self) -> str:
        """Display character rarity with letters ranging from A to SSS, as is done in-game."""
        pass

    @property
    def _type_cn(self) -> str:
        pass

    @property
    def type(self) -> str:
        pass

    @property
    def closeup_icon(self) -> str:
        pass

    @property
    def icon(self) -> str:
        pass

    @property
    def icon_background(self) -> str:
        pass

    @property
    def image(self) -> str:
        pass

    @property
    def cropped_icon(self) -> str:
        pass

    @property
    def banner(self) -> str:
        pass
