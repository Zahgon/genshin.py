"""Utility functions related to genshin."""

import typing
import warnings

from genshin import types

__all__ = [
    "create_short_lang_code",
    "get_prod_game_biz",
    "recognize_game",
    "recognize_genshin_server",
    "recognize_honkai_server",
    "recognize_region",
    "recognize_server",
    "recognize_starrail_server",
    "recognize_zzz_server",
]

UID_RANGE: typing.Mapping[types.Game, typing.Mapping[types.Region, typing.Sequence[str]]] = {
    types.Game.GENSHIN: {
        types.Region.OVERSEAS: ("6", "7", "8", "18", "9"),
        types.Region.CHINESE: ("1", "2", "3", "5"),
    },
    types.Game.STARRAIL: {
        types.Region.OVERSEAS: ("6", "7", "8", "9"),
        types.Region.CHINESE: ("1", "2", "5"),
    },
    types.Game.HONKAI: {
        types.Region.OVERSEAS: ("1", "2"),
        types.Region.CHINESE: ("3", "4"),
    },
}
"""Mapping of games and regions to their respective UID ranges."""

GENSHIN_SERVER_RANGE: typing.Mapping[str, typing.Sequence[str]] = {
    "cn_gf01": ("1", "2", "3"),
    "cn_qd01": ("5",),
    "os_usa": ("6",),
    "os_euro": ("7",),
    "os_asia": ("8", "18"),
    "os_cht": ("9",),
}
"""Mapping of Genshin servers to their respective UID ranges."""

STARRAIL_SERVER_RANGE: typing.Mapping[str, typing.Sequence[str]] = {
    "prod_gf_cn": ("1", "2"),
    "prod_qd_cn": ("5",),
    "prod_official_usa": ("6",),
    "prod_official_eur": ("7",),
    "prod_official_asia": ("8",),
    "prod_official_cht": ("9",),
}
"""Mapping of Star Rail servers to their respective UID ranges."""

ZZZ_SERVER_RANGE: typing.Mapping[str, typing.Sequence[str]] = {
    "prod_gf_us": ("10",),
    "prod_gf_eu": ("15",),
    "prod_gf_jp": ("13",),
    "prod_gf_sg": ("17",),
}
"""Mapping of global Zenless Zone Zero servers to their respective UID ranges."""


def create_short_lang_code(lang: str) -> str:
    """Create an alternative short lang code."""
    pass


def recognize_genshin_server(uid: int) -> str:
    """Recognize which server a Genshin UID is from."""
    pass


def get_prod_game_biz(region: types.Region, game: types.Game) -> str:
    """Get the game_biz value corresponding to a game and region."""
    pass


def recognize_honkai_server(uid: int) -> str:
    """Recognizes which server a Honkai UID is from."""
    pass


def recognize_starrail_server(uid: int) -> str:
    """Recognize which server a Star Rail UID is from."""
    pass


def recognize_zzz_server(uid: int) -> str:
    """Recognize which server a Zenless Zone Zero UID is from."""
    pass


def recognize_server(uid: int, game: types.Game) -> str:
    """Recognizes which server a UID is from."""
    pass


def recognize_game(uid: int, region: types.Region) -> typing.Optional[types.Game]:
    """Recognize the game of a uid."""
    pass


def recognize_region(uid: int, game: types.Game) -> typing.Optional[types.Region]:
    """Recognize the region of a uid."""
    pass
