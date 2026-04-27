"""App sub client for AuthClient.

Covers HoYoLAB and Miyoushe app auth endpoints.
"""

import json
import random
import string
import typing
from http.cookies import SimpleCookie

from genshin import errors
from genshin.client import routes
from genshin.client.components import base
from genshin.models.auth.cookie import AppLoginResult
from genshin.models.auth.geetest import SessionMMT, SessionMMTResult, SessionMMTv4, SessionMMTv4Result
from genshin.models.auth.qrcode import QRCodeCreationResult, QRCodeStatus
from genshin.models.auth.verification import ActionTicket
from genshin.types import AppGeetestResult, AppGeetestSession
from genshin.utility import auth as auth_utility
from genshin.utility import ds as ds_utility

__all__ = ["AppAuthClient"]


class AppAuthClient(base.BaseClient):
    """App sub client for AuthClient."""

    @staticmethod
    def generate_app_device_id() -> str:
        """Generate a random device ID for app login."""
        pass

    @typing.overload
    async def _app_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        device_id: str,
        device_name: typing.Optional[str] = ...,
        device_model: typing.Optional[str] = ...,
        encrypted: bool = ...,
        mmt_result: SessionMMTResult,
        ticket: None = ...,
    ) -> typing.Union[AppLoginResult, ActionTicket]: ...

    @typing.overload
    async def _app_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        device_id: str,
        device_name: typing.Optional[str] = ...,
        device_model: typing.Optional[str] = ...,
        encrypted: bool = ...,
        mmt_result: SessionMMTv4Result,
        ticket: None = ...,
    ) -> typing.Union[AppLoginResult, ActionTicket]: ...

    @typing.overload
    async def _app_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        device_id: str,
        device_name: typing.Optional[str] = ...,
        device_model: typing.Optional[str] = ...,
        encrypted: bool = ...,
        mmt_result: None = ...,
        ticket: ActionTicket,
    ) -> AppLoginResult: ...

    @typing.overload
    async def _app_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        device_id: str,
        device_name: typing.Optional[str] = ...,
        device_model: typing.Optional[str] = ...,
        encrypted: bool = ...,
        mmt_result: None = ...,
        ticket: None = ...,
    ) -> typing.Union[AppLoginResult, SessionMMT, ActionTicket]: ...

    async def _app_login(
        self,
        account: str,
        password: str,
        *,
        device_id: str,
        device_name: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        encrypted: bool = False,
        mmt_result: typing.Optional[AppGeetestResult] = None,
        ticket: typing.Optional[ActionTicket] = None,
    ) -> typing.Union[AppLoginResult, AppGeetestSession, ActionTicket]:
        """Login with a password using HoYoLab app endpoint.

        Returns
        -------
        - AppLoginResult if login is successful.
        - AppGeetestSession if captcha is triggered.
        - ActionTicket if email verification is required.
        """
        pass

    async def _send_verification_email(
        self,
        ticket: ActionTicket,
        *,
        mmt_result: typing.Optional[SessionMMTResult] = None,
    ) -> typing.Union[None, SessionMMT]:
        """Send verification email.

        Returns None if success, SessionMMT data if geetest triggered.
        """
        pass

    async def _verify_email(self, code: str, ticket: ActionTicket) -> None:
        """Verify email."""
        pass

    async def _create_qrcode(self) -> QRCodeCreationResult:
        """Create a QR code for login."""
        pass

    async def _check_qrcode(self, ticket: str) -> tuple[QRCodeStatus, SimpleCookie]:
        """Check the status of a QR code login."""
        pass
