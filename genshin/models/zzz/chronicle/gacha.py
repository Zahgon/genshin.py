import typing

import pydantic

from genshin.models.model import Aliased, APIModel
from genshin.models.zzz.chronicle.events import ZZZGachaEventType

__all__ = (
    "ZZZGachaBannerInfo",
    "ZZZGachaCurrencies",
    "ZZZGachaInfo",
)


class ZZZGachaCurrencies(APIModel):
    """ZZZ gacha currency counts."""

    monochrome: int
    polychrome: int
    encrypted_master_tape: int
    master_tape: int
    boopon: int


class ZZZGachaBannerInfo(APIModel):
    """ZZZ gacha banner info model."""

    type: ZZZGachaEventType = Aliased("gacha_type")
    pity: int = Aliased("more_s_need_cnt")
    """Number of pulls needed until guaranteed S."""


class ZZZGachaInfo(APIModel):
    """ZZZ gacha info model."""

    currencies: ZZZGachaCurrencies
    banners: list[ZZZGachaBannerInfo] = Aliased("gacha_info_list")

    @pydantic.model_validator(mode="before")
    @classmethod
    def __convert_currencies(cls, data: dict[str, typing.Any]) -> dict[str, typing.Any]:
        pass
