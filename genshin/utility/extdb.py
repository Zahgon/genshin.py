"""External databases for Genshin Impact data."""

import asyncio
import json
import logging
import time
import typing
import warnings
from base64 import b64decode as parse_token

import aiohttp

from genshin.constants import LANGS
from genshin.models.genshin import constants as model_constants
from genshin.utility import fs

__all__ = (
    "update_characters_ambr",
    "update_characters_any",
    "update_characters_enka",
    "update_characters_genshindata",
)

LOGGER_ = logging.getLogger(__name__)

CACHE_FILE = fs.get_tempdir() / "characters.json"

if CACHE_FILE.exists() and time.time() - CACHE_FILE.stat().st_mtime < 7 * 24 * 60 * 60:
    names: typing.Mapping[str, typing.Any] = json.loads(CACHE_FILE.read_text())
    try:
        model_constants.CHARACTER_NAMES = {
            lang: {int(char_id): model_constants.DBChar(*char) for char_id, char in chars.items()}
            for lang, chars in names.items()
        }
    except Exception:
        warnings.warn("Failed to load character names from cache")
        CACHE_FILE.unlink()

GENSHINDATA_REPO = parse_token("aHR0cHM6Ly9naXRsYWIuY29tL0RpbWJyZWF0aC9BbmltZUdhbWVEYXRhLy0vcmF3L21hc3Rlci8=").decode()
GENSHINDATA_CHARACTERS_URL = GENSHINDATA_REPO + "ExcelBinOutput/AvatarExcelConfigData.json"
GENSHINDATA_TALENT_DEPOT_URL = GENSHINDATA_REPO + "ExcelBinOutput/AvatarSkillDepotExcelConfigData.json"
GENSHINDATA_TALENT_URL = GENSHINDATA_REPO + "ExcelBinOutput/AvatarSkillExcelConfigData.json"
GENSHINDATA_TEXTMAP_URL = GENSHINDATA_REPO + "TextMap/TextMap{lang}.json"

ENKA_CHARACTERS_URL = "https://raw.githubusercontent.com/EnkaNetwork/API-docs/refs/heads/master/store/gi/avatars.json"
ENKA_LOC_URL = "https://raw.githubusercontent.com/EnkaNetwork/API-docs/refs/heads/master/store/gi/locs.json"

AMBR_URL = "https://gi.yatta.moe/api/v2/{lang}/avatar"
AMBR_VERSION_URL = "https://gi.yatta.moe/api/v2/static/version"

ELEMENTS_MAP: typing.Final[dict[typing.Optional[str], str]] = {
    "Fire": "Pyro",
    "Wind": "Anemo",
    "Ice": "Cryo",
    "Electric": "Electro",
    "Water": "Hydro",
    "Rock": "Geo",
    "Grass": "Dendro",
    "None": "None",
    None: "None",
}
RARITY_MAP = {
    "QUALITY_PURPLE": 4,
    "QUALITY_ORANGE": 5,
    "QUALITY_PURPLE_SP": 104,
    "QUALITY_ORANGE_SP": 105,
}
LANG_MAP = {
    "zh-cn": "chs",
    "zh-tw": "cht",
    "de-de": "de",
    "en-us": "en",
    "es-es": "es",
    "fr-fr": "fr",
    "id-id": "id",
    "it-it": "it",
    "ja-jp": "jp",
    "ko-kr": "kr",
    "pt-pt": "pt",
    "ru-ru": "ru",
    "th-th": "th",
    "vi-vn": "vi",
    "tr-tr": "tr",
}
ENKA_LANG_MAP = {
    "zh-CN": "zh-cn",
    "zh-TW": "zh-tw",
    "de": "de-de",
    "en": "en-us",
    "es": "es-es",
    "fr": "fr-fr",
    "id": "id-id",
    "it": "it-it",
    "ja": "ja-jp",
    "ko": "ko-kr",
    "pt": "pt-pt",
    "ru": "ru-ru",
    "th": "th-th",
    "vi": "vi-vn",
    "tr": "tr",
}


async def _fetch_jsons(*urls: str) -> typing.Sequence[typing.Any]:
    """Fetch multiple JSON endpoints."""
    pass


def update_character_name(
    lang: str,
    id: int,
    icon_name: str,
    name: str,
    element: str,
    rarity: int,
) -> None:
    """Update the character names for a specific language."""
    pass


async def update_characters_genshindata(langs: typing.Sequence[str] = ()) -> None:
    """Update characters with https://github.com/Dimbreath/GenshinData/.

    This method requires the download of >20MB per language so it's not recommended.
    """
    pass


async def update_characters_enka(langs: typing.Sequence[str] = ()) -> None:
    """Update characters with https://github.com/EnkaNetwork/API-docs/."""
    pass


async def update_characters_ambr(langs: typing.Sequence[str] = ()) -> None:
    """Update characters with https://ambr.top/."""
    pass


async def update_characters_any(
    langs: typing.Union[str, typing.Sequence[str], None] = None,
    *,
    lenient: bool = False,
) -> None:
    """Update characters with the most efficient resource.

    Will not re-request data if lenient is True.
    """
    pass
