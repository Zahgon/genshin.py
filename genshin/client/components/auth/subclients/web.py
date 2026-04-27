"""Web sub client for AuthClient.

Covers HoYoLAB and Miyoushe web auth endpoints.
"""

import json
import typing
import uuid

from genshin import constants, errors, types
from genshin.client import routes
from genshin.client.components import base
from genshin.models.auth.cookie import CNWebLoginResult, MobileLoginResult, WebLoginResult
from genshin.models.auth.geetest import SessionMMT, SessionMMTResult, SessionMMTv4
from genshin.utility import auth as auth_utility
from genshin.utility import ds as ds_utility

__all__ = ["WebAuthClient"]


class WebAuthClient(base.BaseClient):
    """Web sub client for AuthClient."""

    @staticmethod
    def generate_web_device_id() -> str:
        """Generate a random device ID for web login."""
        pass

    @typing.overload
    async def _os_web_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        device_id: str,
        encrypted: bool = ...,
        token_type: typing.Optional[int] = ...,
        mmt_result: SessionMMTResult,
    ) -> WebLoginResult: ...

    @typing.overload
    async def _os_web_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        device_id: str,
        encrypted: bool = ...,
        token_type: typing.Optional[int] = ...,
        mmt_result: None = ...,
    ) -> typing.Union[SessionMMT, WebLoginResult]: ...

    @base.region_specific(types.Region.OVERSEAS)
    async def _os_web_login(
        self,
        account: str,
        password: str,
        *,
        device_id: str,
        encrypted: bool = False,
        token_type: typing.Optional[int] = 6,
        mmt_result: typing.Optional[SessionMMTResult] = None,
    ) -> typing.Union[SessionMMT, WebLoginResult]:
        """Login with a password using web endpoint.

        Returns either data from aigis header or cookies.
        """
        pass

    @typing.overload
    async def _cn_web_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = ...,
        mmt_result: SessionMMTResult,
    ) -> CNWebLoginResult: ...

    @typing.overload
    async def _cn_web_login(  # noqa: D102 missing docstring in overload?
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = ...,
        mmt_result: None = ...,
    ) -> typing.Union[SessionMMT, CNWebLoginResult]: ...

    @base.region_specific(types.Region.CHINESE)
    async def _cn_web_login(
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = False,
        mmt_result: typing.Optional[SessionMMTResult] = None,
    ) -> typing.Union[SessionMMT, CNWebLoginResult]:
        """
        Login with account and password using Miyoushe loginByPassword endpoint.

        Returns data from aigis header or cookies.
        """
        pass

    async def _send_mobile_otp(
        self,
        mobile: str,
        *,
        encrypted: bool = False,
        mmt_result: typing.Optional[SessionMMTResult] = None,
    ) -> typing.Union[None, SessionMMTv4]:
        """Attempt to send OTP to the provided mobile number.

        May return aigis headers if captcha is triggered, None otherwise.
        """
        pass

    async def _login_with_mobile_otp(self, mobile: str, otp: str, *, encrypted: bool = False) -> MobileLoginResult:
        """Login with OTP and mobile number.

        Returns cookies if OTP matches the one sent, raises an error otherwise.
        """
        pass
