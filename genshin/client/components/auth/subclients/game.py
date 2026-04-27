"""Game sub client for AuthClient.

Covers OS and CN game auth endpoints.
"""

import json
import typing

from genshin import constants, errors
from genshin.client import routes
from genshin.client.components import base
from genshin.models.auth.cookie import DeviceGrantResult, GameLoginResult
from genshin.models.auth.geetest import RiskyCheckMMT, RiskyCheckMMTResult, RiskyCheckResult
from genshin.models.auth.responses import ShieldLoginResponse
from genshin.utility import auth as auth_utility

__all__ = ["GameAuthClient"]


class GameAuthClient(base.BaseClient):
    """Game sub client for AuthClient."""

    async def _risky_check(
        self, action_type: str, api_name: str, *, username: typing.Optional[str] = None
    ) -> RiskyCheckResult:
        """Check if the given action (endpoint) is risky (whether captcha verification is required)."""
        pass

    @typing.overload
    async def _shield_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = ...,
        mmt_result: RiskyCheckMMTResult,
    ) -> ShieldLoginResponse: ...

    @typing.overload
    async def _shield_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = ...,
        mmt_result: None = ...,
    ) -> typing.Union[ShieldLoginResponse, RiskyCheckMMT]: ...

    async def _shield_login(
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = False,
        mmt_result: typing.Optional[RiskyCheckMMTResult] = None,
    ) -> typing.Union[ShieldLoginResponse, RiskyCheckMMT]:
        """Log in with the given account and password.

        Returns MMT if geetest verification is required.
        """
        pass

    @typing.overload
    async def _send_game_verification_email(  # noqa: D102 missing docstring in overload?
        self,
        action_ticket: str,
        *,
        device_model: typing.Optional[str] = None,
        device_name: typing.Optional[str] = None,
        client_type: typing.Optional[int] = None,
        mmt_result: RiskyCheckMMTResult,
    ) -> None: ...

    @typing.overload
    async def _send_game_verification_email(  # noqa: D102 missing docstring in overload?
        self,
        action_ticket: str,
        *,
        device_model: typing.Optional[str] = None,
        device_name: typing.Optional[str] = None,
        client_type: typing.Optional[int] = None,
        mmt_result: None = ...,
    ) -> typing.Union[None, RiskyCheckMMT]: ...

    async def _send_game_verification_email(
        self,
        action_ticket: str,
        *,
        device_model: typing.Optional[str] = None,
        device_name: typing.Optional[str] = None,
        client_type: typing.Optional[int] = None,
        mmt_result: typing.Optional[RiskyCheckMMTResult] = None,
    ) -> typing.Union[None, RiskyCheckMMT]:
        """Send email verification code.

        Returns `None` if success, `RiskyCheckMMT` if geetest verification is required.
        """
        pass

    async def _verify_game_email(self, code: str, action_ticket: str) -> DeviceGrantResult:
        """Verify the email code."""
        pass

    async def _os_game_login(self, uid: str, game_token: str) -> GameLoginResult:
        """Log in to the game."""
        pass
