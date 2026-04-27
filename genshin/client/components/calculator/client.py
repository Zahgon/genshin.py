"""Calculator client."""

from __future__ import annotations

import asyncio
import typing
import warnings

import aiohttp.typedefs

import genshin.models.genshin as genshin_models
from genshin import errors, types, utility
from genshin.client import cache as client_cache
from genshin.client import routes
from genshin.client.components import base
from genshin.models.genshin import calculator as models
from genshin.utility import deprecation

from .calculator import BatchCalculator, Calculator, FurnishingCalculator

__all__ = ["CalculatorClient"]


class CalculatorClient(base.BaseClient):
    """Calculator component."""

    async def request_calculator(
        self,
        endpoint: str,
        *,
        method: str = "POST",
        lang: typing.Optional[str] = None,
        params: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        data: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        headers: typing.Optional[aiohttp.typedefs.LooseHeaders] = None,
        api_version: int = 1,
        **kwargs: typing.Any,
    ) -> typing.Mapping[str, typing.Any]:
        """Make a request towards the calculator endpoint."""
        pass

    async def _execute_calculator(
        self,
        data: typing.Mapping[str, typing.Any],
        *,
        lang: typing.Optional[str] = None,
    ) -> models.CalculatorResult:
        """Calculate the results of a builder."""
        pass

    async def _execute_batch_calculator(
        self,
        data: typing.Sequence[typing.Mapping[str, typing.Any]],
        *,
        lang: typing.Optional[str] = None,
    ) -> models.CalculatorBatchResult:
        """Calculate the results of a batch builder."""
        pass

    async def _execute_furnishings_calculator(
        self,
        data: typing.Mapping[str, typing.Any],
        *,
        lang: typing.Optional[str] = None,
    ) -> models.CalculatorFurnishingResults:
        """Calculate the results of a builder."""
        pass

    def calculator(self, *, lang: typing.Optional[str] = None) -> Calculator:
        """Create a calculator builder object."""
        pass

    def batch_calculator(self, *, lang: typing.Optional[str] = None) -> BatchCalculator:
        """Create a batch calculator builder object."""
        pass

    def furnishings_calculator(self, *, lang: typing.Optional[str] = None) -> FurnishingCalculator:
        """Create a calculator builder object."""
        pass

    async def _enable_calculator_sync(self, enabled: bool = True) -> None:
        """Enable data syncing in calculator."""
        pass

    async def _get_calculator_items(
        self,
        slug: str,
        filters: typing.Mapping[str, typing.Any],
        query: typing.Optional[str] = None,
        *,
        uid: typing.Optional[int] = None,
        is_all: bool = False,
        sync: bool = False,
        lang: typing.Optional[str] = None,
        autoauth: bool = True,
    ) -> typing.Sequence[typing.Mapping[str, typing.Any]]:
        """Get all items of a specific slug from a calculator."""
        pass

    async def get_calculator_characters(
        self,
        *,
        query: typing.Optional[str] = None,
        elements: typing.Optional[typing.Sequence[int]] = None,
        weapon_types: typing.Optional[typing.Sequence[int]] = None,
        include_traveler: bool = False,
        sync: bool = False,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.CalculatorCharacter]:
        """Get all characters provided by the Enhancement Progression Calculator."""
        pass

    async def get_calculator_weapons(
        self,
        *,
        query: typing.Optional[str] = None,
        types: typing.Optional[typing.Sequence[int]] = None,
        rarities: typing.Optional[typing.Sequence[int]] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.CalculatorWeapon]:
        """Get all weapons provided by the Enhancement Progression Calculator."""
        pass

    async def get_calculator_artifacts(
        self,
        *,
        query: typing.Optional[str] = None,
        pos: int = 1,
        rarities: typing.Optional[typing.Sequence[int]] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.CalculatorArtifact]:
        """Get all artifacts provided by the Enhancement Progression Calculator."""
        pass

    async def get_calculator_furnishings(
        self,
        *,
        types: typing.Optional[int] = None,
        rarities: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.CalculatorFurnishing]:
        """Get all furnishings provided by the Enhancement Progression Calculator."""
        pass

    async def get_character_details(
        self,
        character: types.IDOr[genshin_models.BaseCharacter],
        *,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> models.CalculatorCharacterDetails:
        """Get the weapon, artifacts and talents of a character.

        Not related to the Battle Chronicle.
        This data is always private.
        """
        pass

    async def get_complete_artifact_set(
        self,
        artifact: types.IDOr[typing.Union[genshin_models.Artifact, genshin_models.CalculatorArtifact]],
        *,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.CalculatorArtifact]:
        """Get all other artifacts that share a set with any given artifact.

        Doesn't return the artifact passed into this function.
        """
        pass

    async def _get_all_artifact_ids(self, artifact_id: int) -> typing.Sequence[int]:
        """Get all artifact ids in the same set as a given artifact id."""
        pass

    async def get_teapot_replica_blueprint(
        self,
        share_code: int,
        *,
        region: typing.Optional[str] = None,
        uid: typing.Optional[int] = None,
        lang: typing.Optional[str] = None,
    ) -> typing.Sequence[models.CalculatorFurnishing]:
        """Get furnishings used by a teapot replica blueprint."""
        pass

    @deprecation.deprecated("await genshin.utility.update_characters_any()")
    async def update_character_names(self, *, lang: typing.Optional[str] = None) -> None:
        """Update stored db characters with the names from the calculator."""
        pass
