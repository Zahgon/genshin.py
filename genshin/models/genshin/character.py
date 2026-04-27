"""Genshin character model."""

import logging
import re
import typing

import pydantic

from genshin.models.model import APIModel, Unique
from genshin.utility import deprecation

from . import constants

__all__ = ["BaseCharacter"]

_LOGGER = logging.getLogger(__name__)

ENKA_ICON_BASE = "https://enka.network/ui/"
AMBR_ICON_BASE = "https://gi.yatta.moe/assets/UI/"


def _parse_icon(icon: typing.Union[str, int]) -> str:
    pass


def _get_icon_name_from_id(character_id: int) -> str:
    pass


def _create_icon(icon: str, specifier: str) -> str:
    pass


def _create_icon_from_id(character_id: int, specifier: str) -> str:
    pass


def _get_db_char(
    id: typing.Optional[int] = None,
    name: typing.Optional[str] = None,
    icon: typing.Optional[str] = None,
    element: typing.Optional[str] = None,
    rarity: typing.Optional[int] = None,
    *,
    lang: str,
) -> constants.DBChar:
    """Get the appropriate DBChar object from specific fields."""
    pass


class BaseCharacter(APIModel, Unique):
    """Base character model."""

    id: int
    name: str
    element: str
    rarity: int
    icon: str

    collab: bool = False

    @pydantic.model_validator(mode="before")
    def __autocomplete(cls, values: dict[str, typing.Any]) -> dict[str, typing.Any]:
        """Complete missing data."""
        pass

    @property
    @deprecation.deprecated("gacha_art")
    def image(self) -> str:
        pass

    @property
    def gacha_art(self) -> str:
        pass

    @property
    def side_icon(self) -> str:
        pass

    @property
    def card_icon(self) -> str:
        pass

    @property
    def traveler_name(self) -> str:
        pass
