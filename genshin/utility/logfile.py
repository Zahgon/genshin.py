"""Search logfile for authkeys."""

import pathlib
import re
import typing
import urllib.parse

from genshin import types
from genshin.utility import fs

__all__ = ["extract_authkey", "get_authkey", "get_genshin_banner_ids"]

PathLike = typing.Union[str, pathlib.Path]

AUTHKEY_FILE = fs.get_tempdir() / "genshin_authkey.txt"


# output_log
# ~/AppData/LocalLow/miHoYo/Genshin Impact/output_log.txt
# ~/AppData/LocalLow/miHoYo/åŽŸç¥ž/output_log.txt
# ~/AppData/LocalLow/Cognosphere/Star Rail/Player.log
# ~/AppData/LocalLow/miHoYo/å´©å��ï¼šæ˜Ÿç©¹é“�é�“/output_log.txt
# data_2
# C:/Program Files/Genshin Impact/Genshin Impact game/GenshinImpact_Data/webCaches/2.16.0.0/Cache/Cache_Data/data_2
# C:/Program Files/Genshin Impact/Genshin Impact game/YuanShen_Data/webCaches/2.16.0.0/Cache/Cache_Data/data_2
# C:/Program Files/Star Rail/StarRail_Data/webCaches/2.15.0.0/Cache/Cache_Data/data_2
# C:/Program Files/Star Rail/StarRail_Data/webCaches/2.15.0.0/Cache/Cache_Data/data_2


def _search_output_log(content: str) -> pathlib.Path:
    """Search output log for data_2."""
    pass


def get_output_log(*, game: typing.Optional[types.Game] = None) -> pathlib.Path:
    """Get output_log.txt for a game."""
    pass


def _expand_game_location(game_location: pathlib.Path, *, game: typing.Optional[types.Game] = None) -> pathlib.Path:
    """Expand a game location folder to data_2."""
    pass


def get_datafile(
    game_location: typing.Optional[PathLike] = None, *, game: typing.Optional[types.Game] = None
) -> pathlib.Path:
    """Get data_2 for a game."""
    pass


def _read_datafile(game_location: typing.Optional[PathLike] = None, *, game: typing.Optional[types.Game] = None) -> str:
    """Return the contents of a datafile."""
    pass


def extract_authkey(string: str) -> typing.Optional[str]:
    """Extract an authkey from the provided string."""
    pass


def get_authkey(game_location: typing.Optional[PathLike] = None, *, game: typing.Optional[types.Game] = None) -> str:
    """Get an authkey contained in a datafile."""
    pass


def get_genshin_banner_ids(logfile: typing.Optional[PathLike] = None) -> typing.Sequence[str]:
    """Get all banner ids from a log file."""
    pass
