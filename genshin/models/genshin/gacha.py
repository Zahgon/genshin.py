"""Genshin wish models."""

import datetime
import enum
import re
import typing

import pydantic

from genshin.models.model import Aliased, APIModel, Unique

__all__ = [
    "BannerDetailItem",
    "BannerDetails",
    "BannerDetailsUpItem",
    "GachaItem",
    "GenshinBannerType",
    "MWBannerType",
    "MWWish",
    "SignalSearch",
    "StarRailBannerType",
    "Warp",
    "Wish",
    "ZZZBannerType",
]


class GenshinBannerType(enum.IntEnum):
    """Banner types in wish histories."""

    NOVICE = 100
    """Temporary novice banner."""

    STANDARD = PERMANENT = 200
    """Permanent standard banner."""

    CHARACTER = 301
    """Rotating character banner."""

    WEAPON = 302
    """Rotating weapon banner."""

    CHRONICLED = 500
    """Chronicled banner."""

    # these are special cases
    # they exist inside the history but should be counted as the same

    CHARACTER1 = 301
    """Character banner #1."""

    CHARACTER2 = 400
    """Character banner #2."""


class MWBannerType(enum.IntEnum):
    """Banner types in Genshin Miliastra Wonderland."""

    STANDARD = PERMANENT = 1000
    """Permanent standard banner."""

    EVENT = 2000
    """Event banner."""

    EVENT_MALE_OUTFIT1 = 20011
    """Male Manekin outfit banner #1."""

    EVENT_MALE_OUTFIT2 = 20012
    """Male Manekin outfit banner #2."""

    EVENT_FEMALE_OUTFIT1 = 20021
    """Female Manekin outfit banner #1."""

    EVENT_FEMALE_OUTFIT2 = 20022
    """Female Manekin outfit banner #2."""


class StarRailBannerType(enum.IntEnum):
    """Banner types in wish histories."""

    STANDARD = PERMANENT = 1
    """Permanent standard banner."""
    NOVICE = 2
    """Temporary novice banner."""
    CHARACTER = 11
    """Rotating character banner."""
    WEAPON = 12
    """Rotating light cone banner."""

    FATE_CHARACTER = 21
    """FGO collab character banner."""
    FATE_WEAPON = 22
    """FGO collab light cone banner."""


class ZZZBannerType(enum.IntEnum):
    """Banner types in wish histories."""

    STANDARD = PERMANENT = 1
    """Permanent standard banner."""

    CHARACTER = 2
    """Rotating character banner."""

    WEAPON = 3
    """Rotating w-engine banner."""

    BANGBOO = 5
    """Bangboo banner."""

    EXCLUSIVE_RESCREENING = 102
    """Exclusive rescreening banner."""

    REVERBERATION = 103
    """W-Engine reverberation banner."""

    def to_chronicle_type(self) -> str:
        """Get the chronicle type string for this banner type."""
        pass


class BaseWish(APIModel, Unique):
    """Base wish model."""

    uid: int
    id: int
    name: str
    rarity: int = Aliased("rank_type")

    tz_offset: int
    """Number of hours from UTC+8."""
    time: datetime.datetime
    """Timezone-aware time of when the wish was made"""

    @pydantic.field_validator("rarity", mode="before")
    def __cast_rarity(cls, v: typing.Any) -> int:
        pass

    @pydantic.field_validator("time", mode="before")
    def __parse_time(cls, v: str, info: pydantic.ValidationInfo) -> datetime.datetime:
        pass


class Wish(BaseWish):
    """Wish made on any banner."""

    type: str = Aliased("item_type")
    banner_type: GenshinBannerType

    @pydantic.field_validator("banner_type", mode="before")
    def __cast_banner_type(cls, v: typing.Any) -> int:
        pass


class MWWish(BaseWish):
    """Wish made on Genshin Miliastra Wonderland banner."""

    item_id: int
    type: str = Aliased("item_type")
    is_up: bool
    name: str = Aliased("item_name")

    banner_id: int = Aliased("schedule_id")
    banner_type: MWBannerType = Aliased("op_gacha_type")


class Warp(BaseWish):
    """Warp made on any banner."""

    item_id: int
    type: str = Aliased("item_type")

    banner_type: StarRailBannerType
    banner_id: int = Aliased("gacha_id")

    @pydantic.field_validator("banner_type", mode="before")
    def __cast_banner_type(cls, v: typing.Any) -> int:
        pass


class SignalSearch(BaseWish):
    """Signal Search made on any banner."""

    item_id: int
    type: str = Aliased("item_type")

    banner_type: ZZZBannerType

    @pydantic.field_validator("banner_type", mode="before")
    def __cast_banner_type(cls, v: typing.Any) -> int:
        pass

    @classmethod
    def from_chronicle_data(
        cls, data: typing.Mapping[str, typing.Any], uid: int, tz_offset: int, banner_type: ZZZBannerType
    ) -> "SignalSearch":
        """Create a ZZZChronicleWish from chronicle data."""
        pass


class BannerDetailItem(APIModel):
    """Item that may be gotten from a banner."""

    name: str = Aliased("item_name")
    type: str = Aliased("item_type")
    rarity: int = Aliased("rank")

    up: bool = Aliased("is_up")
    order: int = Aliased("order_value")


class BannerDetailsUpItem(APIModel):
    """Item that has a rate-up on a banner."""

    name: str = Aliased("item_name")
    type: str = Aliased("item_type")
    element: str = Aliased("item_attr")
    icon: str = Aliased("item_img")

    @pydantic.field_validator("element", mode="before")
    def __parse_element(cls, v: str) -> str:
        pass


class BannerDetails(APIModel):
    """Details of a banner."""

    banner_id: str
    banner_type: int = Aliased("gacha_type")
    title: str
    content: str
    date_range: str

    r5_up_prob: typing.Optional[float]
    r4_up_prob: typing.Optional[float]
    r5_prob: typing.Optional[float]
    r4_prob: typing.Optional[float]
    r3_prob: typing.Optional[float]
    r5_guarantee_prob: typing.Optional[float] = Aliased("r5_baodi_prob")
    r4_guarantee_prob: typing.Optional[float] = Aliased("r4_baodi_prob")
    r3_guarantee_prob: typing.Optional[float] = Aliased("r3_baodi_prob")

    r5_up_items: typing.Sequence[BannerDetailsUpItem]
    r4_up_items: typing.Sequence[BannerDetailsUpItem]

    r5_items: list[BannerDetailItem] = Aliased("r5_prob_list")
    r4_items: list[BannerDetailItem] = Aliased("r4_prob_list")
    r3_items: list[BannerDetailItem] = Aliased("r3_prob_list")

    @pydantic.field_validator("r5_up_items", "r4_up_items", mode="before")
    def __replace_none(cls, v: typing.Optional[typing.Sequence[typing.Any]]) -> typing.Sequence[typing.Any]:
        pass

    @pydantic.field_validator(
        "r5_up_prob",
        "r4_up_prob",
        "r5_prob",
        "r4_prob",
        "r3_prob",
        "r5_guarantee_prob",
        "r4_guarantee_prob",
        "r3_guarantee_prob",
        mode="before",
    )
    def __parse_percentage(cls, v: typing.Optional[str]) -> typing.Optional[float]:
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def banner_type_name(self) -> str:
        pass

    @property
    def items(self) -> typing.Sequence[BannerDetailItem]:
        pass


class GachaItem(APIModel, Unique):
    """Item that can be gotten from the gacha."""

    name: str
    type: str = Aliased("item_type")
    rarity: int = Aliased("rank_type")
    id: int = Aliased("item_id")

    @pydantic.field_validator("id")
    def __format_id(cls, v: int) -> int:
        pass

    def is_character(self) -> bool:
        """Whether this item is a character."""
        pass
