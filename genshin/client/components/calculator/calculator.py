"""Calculator builder object.

Over-engineered for the sake of extendability and maintainability.
"""

from __future__ import annotations

import abc
import asyncio
import typing

import genshin.models.genshin as genshin_models
from genshin import types
from genshin.models.genshin import calculator as models

if typing.TYPE_CHECKING:
    from .client import CalculatorClient as Client

__all__ = ["Calculator", "FurnishingCalculator"]

T = typing.TypeVar("T")
CallableT = typing.TypeVar("CallableT", bound="typing.Callable[..., typing.Awaitable[object]]")


def _cache(func: CallableT) -> CallableT:
    """Cache a method."""
    pass


class CalculatorState:
    """Stores character details if multiple objects require them."""

    client: Client
    cache: dict[str, typing.Any]
    lock: asyncio.Lock

    character_id: typing.Optional[int] = None

    def __init__(self, client: Client) -> None:
        self.client = client
        self.cache = {}
        self.lock = asyncio.Lock()

    @_cache
    async def get_character_details(self) -> models.CalculatorCharacterDetails:
        """Get character details."""
        pass

    @_cache
    async def get_artifact_ids(self, artifact_id: int) -> typing.Sequence[int]:
        """Get artifact ids."""
        pass


class CalculatorResolver(abc.ABC, typing.Generic[T]):
    """Auto-resolving calculator object."""

    @abc.abstractmethod
    async def __call__(self, state: CalculatorState) -> T:
        """Resolve the object into concrete data."""


class CharacterResolver(CalculatorResolver[typing.Mapping[str, typing.Any]]):
    def __init__(
        self,
        character: types.IDOr[genshin_models.BaseCharacter],
        current: typing.Optional[int] = None,
        target: typing.Optional[int] = None,
        *,
        element: typing.Optional[int] = None,
    ) -> None:
        if isinstance(character, genshin_models.BaseCharacter):
            current = current or getattr(character, "level", None)
            character = character.id

        self.id = character
        self.current = current
        self.target = target
        self.element = element

    async def __call__(self, state: CalculatorState) -> typing.Mapping[str, typing.Any]:
        if self.current is None or self.target is None:
            return {}

        data = dict(
            avatar_id=self.id,
            avatar_level_current=self.current,
            avatar_level_target=self.target,
        )
        if self.element:
            data.update(element_attr_id=self.element)

        return data


class WeaponResolver(CalculatorResolver[typing.Mapping[str, typing.Any]]):
    id: int
    current: int
    target: int

    def __init__(self, weapon: int, current: int, target: int) -> None:
        self.id = weapon
        self.current = current
        self.target = target

    async def __call__(self, state: CalculatorState) -> typing.Mapping[str, typing.Any]:
        return dict(
            id=self.id,
            level_current=self.current,
            level_target=self.target,
        )


class CurrentWeaponResolver(WeaponResolver):
    id: int
    current: int
    target: int

    def __init__(self, target: int):
        self.target = target

    async def __call__(self, state: CalculatorState) -> typing.Mapping[str, typing.Any]:
        details = await state.get_character_details()
        self.id = details.weapon.id
        self.current = details.weapon.level
        return await super().__call__(state)


class ArtifactResolver(CalculatorResolver[typing.Sequence[typing.Mapping[str, typing.Any]]]):
    data: list[typing.Mapping[str, typing.Any]]

    def __init__(self) -> None:
        self.data = []

    def add_artifact(self, id: int, current: int, target: int) -> None:
        pass

    async def __call__(self, state: CalculatorState) -> typing.Sequence[typing.Mapping[str, typing.Any]]:
        return self.data


class ArtifactSetResolver(ArtifactResolver):
    def __init__(self, any_artifact_id: int, current: int, target: int) -> None:
        self.id = any_artifact_id
        self.current = current
        self.target = target

        super().__init__()

    async def __call__(self, state: CalculatorState) -> typing.Sequence[typing.Mapping[str, typing.Any]]:
        artifact_ids = await state.get_artifact_ids(self.id)

        for artifact_id in artifact_ids:
            self.add_artifact(artifact_id, self.current, self.target)

        return self.data


class CurrentArtifactResolver(ArtifactResolver):
    artifacts: typing.Sequence[typing.Optional[int]]

    def __init__(
        self,
        target: typing.Optional[int] = None,
        *,
        flower: typing.Optional[int] = None,
        feather: typing.Optional[int] = None,
        sands: typing.Optional[int] = None,
        goblet: typing.Optional[int] = None,
        circlet: typing.Optional[int] = None,
    ) -> None:
        if target:
            self.artifacts = (target,) * 5
        else:
            self.artifacts = (flower, feather, sands, goblet, circlet)

        super().__init__()

    async def __call__(self, state: CalculatorState) -> typing.Sequence[typing.Mapping[str, typing.Any]]:
        details = await state.get_character_details()

        for artifact in details.artifacts:
            if target := self.artifacts[artifact.pos - 1]:
                self.add_artifact(artifact.id, artifact.level, target)

        return self.data


class TalentResolver(CalculatorResolver[typing.Sequence[typing.Mapping[str, typing.Any]]]):
    data: list[typing.Mapping[str, typing.Any]]

    def __init__(self) -> None:
        self.data = []

    def add_talent(self, id: int, current: int, target: int) -> None:
        pass

    async def __call__(self, state: CalculatorState) -> typing.Sequence[typing.Mapping[str, typing.Any]]:
        return self.data


class CurrentTalentResolver(TalentResolver):
    talents: typing.Mapping[str, typing.Optional[int]]

    def __init__(
        self,
        target: typing.Optional[int] = None,
        current: typing.Optional[int] = None,
        *,
        attack: typing.Optional[int] = None,
        skill: typing.Optional[int] = None,
        burst: typing.Optional[int] = None,
    ) -> None:
        self.current = current
        if target:
            self.talents = {
                "attack": target,
                "skill": target,
                "burst": target,
            }
        else:
            self.talents = {
                "attack": attack,
                "skill": skill,
                "burst": burst,
            }

        super().__init__()

    async def __call__(self, state: CalculatorState) -> typing.Sequence[typing.Mapping[str, typing.Any]]:
        details = await state.get_character_details()
        talents = details.talents

        if talents[2].type == "dash":
            ordered = (talents[0], talents[1], talents[3])
        else:
            ordered = (talents[0], talents[1], talents[2])

        for talent, name in zip(ordered, ("attack", "skill", "burst")):
            if target := self.talents[name]:
                self.add_talent(talent.group_id, self.current if self.current is not None else talent.level, target)

        return self.data


class Calculator:
    """Builder for the genshin impact enhancement calculator."""

    client: Client
    lang: typing.Optional[str]

    character: typing.Optional[CharacterResolver]
    weapon: typing.Optional[WeaponResolver]
    artifacts: typing.Optional[ArtifactResolver]
    talents: typing.Optional[TalentResolver]

    _state: CalculatorState

    def __init__(self, client: Client, *, lang: typing.Optional[str] = None) -> None:
        self.client = client
        self.lang = lang

        self.character = None
        self.weapon = None
        self.artifacts = None
        self.talents = None

        self._state = CalculatorState(client)

    def set_character(
        self,
        character: types.IDOr[genshin_models.BaseCharacter],
        current: typing.Optional[int] = None,
        target: typing.Optional[int] = None,
        *,
        element: typing.Optional[int] = None,
    ) -> Calculator:
        """Set the character."""
        pass

    def set_weapon(self, id: int, current: int, target: int) -> Calculator:
        """Set the weapon."""
        pass

    def add_artifact(self, id: int, current: int, target: int) -> Calculator:
        """Add an artifact."""
        pass

    def set_artifact_set(self, any_artifact_id: int, current: int, target: int) -> Calculator:
        """Set an artifact set."""
        pass

    def add_talent(self, group_id: int, current: int, target: int) -> Calculator:
        """Add a talent."""
        pass

    def with_current_weapon(self, target: int) -> Calculator:
        """Set the weapon of the selected character."""
        pass

    def with_current_artifacts(
        self,
        target: typing.Optional[int] = None,
        *,
        flower: typing.Optional[int] = None,
        feather: typing.Optional[int] = None,
        sands: typing.Optional[int] = None,
        goblet: typing.Optional[int] = None,
        circlet: typing.Optional[int] = None,
    ) -> Calculator:
        """Add all artifacts of the selected character."""
        pass

    def with_current_talents(
        self,
        target: typing.Optional[int] = None,
        current: typing.Optional[int] = None,
        *,
        attack: typing.Optional[int] = None,
        skill: typing.Optional[int] = None,
        burst: typing.Optional[int] = None,
    ) -> Calculator:
        """Add all talents of the currently selected character."""
        pass

    async def build(self) -> typing.Mapping[str, typing.Any]:
        """Build the calculator object."""
        pass

    async def calculate(self) -> models.CalculatorResult:
        """Execute the calculator."""
        pass

    def __await__(self) -> typing.Generator[typing.Any, None, models.CalculatorResult]:
        return self.calculate().__await__()


class BatchCalculator:
    """Builder for the genshin impact batch enhancement calculator."""

    client: Client
    lang: typing.Optional[str]

    characters: list[Calculator]

    def __init__(self, client: Client, *, lang: typing.Optional[str] = None) -> None:
        self.client = client
        self.lang = lang

        self.characters = []

    def add_character(self, builder: Calculator) -> BatchCalculator:
        """Add a character."""
        pass

    async def build(self) -> typing.Sequence[typing.Mapping[str, typing.Any]]:
        """Build the calculator object."""
        pass

    async def calculate(self) -> models.CalculatorBatchResult:
        """Execute the calculator."""
        pass

    def __await__(self) -> typing.Generator[typing.Any, None, models.CalculatorBatchResult]:
        return self.calculate().__await__()


class FurnishingCalculator:
    """Builder for the genshin impact furnishing calculator."""

    client: Client
    lang: typing.Optional[str]

    furnishings: dict[int, int]
    replica_code: typing.Optional[int] = None
    replica_region: typing.Optional[str] = None

    def __init__(self, client: Client, *, lang: typing.Optional[str] = None) -> None:
        self.client = client
        self.lang = lang

        self.furnishings = {}
        self.replica_code = None
        self.replica_region = None

    def add_furnishing(self, id: types.IDOr[models.CalculatorFurnishing], amount: int = 1) -> FurnishingCalculator:
        """Add a furnishing."""
        pass

    def with_replica(self, code: int, *, region: typing.Optional[str] = None) -> FurnishingCalculator:
        """Set the replica code."""
        pass

    async def build(self) -> typing.Mapping[str, typing.Any]:
        """Build the calculator object."""
        pass

    async def calculate(self) -> models.CalculatorFurnishingResults:
        """Execute the calculator."""
        pass

    def __await__(self) -> typing.Generator[typing.Any, None, models.CalculatorFurnishingResults]:
        return self.calculate().__await__()
