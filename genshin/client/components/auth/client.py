"""Main auth client."""

import asyncio
import json
import logging
import random
import time
import typing
import uuid
from string import digits

import aiohttp

from genshin import constants, errors, types
from genshin.client import routes
from genshin.client.components import base
from genshin.client.manager import managers
from genshin.models.auth.cookie import (
    AppLoginResult,
    CNWebLoginResult,
    GameLoginResult,
    MobileLoginResult,
    QRLoginResult,
    WebLoginResult,
)
from genshin.models.auth.geetest import (
    MMT,
    MMTResult,
    RiskyCheckMMT,
    RiskyCheckMMTResult,
    SessionMMT,
    SessionMMTResult,
    SessionMMTv4,
)
from genshin.models.auth.qrcode import QRCodeStatus
from genshin.models.auth.verification import ActionTicket
from genshin.utility import auth as auth_utility
from genshin.utility import ds as ds_utility

from . import server, subclients

__all__ = ["AuthClient"]

LOGGER_ = logging.getLogger(__name__)


class AuthClient(subclients.AppAuthClient, subclients.WebAuthClient, subclients.GameAuthClient):
    """Auth client component."""

    async def login_with_password(
        self,
        account: str,
        password: str,
        *,
        port: int = 5000,
        encrypted: bool = False,
        geetest_solver: typing.Optional[typing.Callable[[SessionMMT], typing.Awaitable[SessionMMTResult]]] = None,
    ) -> typing.Union[WebLoginResult, CNWebLoginResult]:
        """Login with a password via web endpoint.

        Endpoint is chosen based on client region.

        Note that this will start a webserver if captcha is
        triggered and `geetest_solver` is not passed.

        Raises
        ------
        - AccountLoginFail: Invalid password provided.
        - AccountDoesNotExist: Invalid email/username.
        """
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def os_login_with_password(
        self,
        account: str,
        password: str,
        *,
        port: int = 5000,
        encrypted: bool = False,
        token_type: typing.Optional[int] = 6,
        geetest_solver: typing.Optional[typing.Callable[[SessionMMT], typing.Awaitable[SessionMMTResult]]] = None,
    ) -> WebLoginResult:
        """Login with a password via web endpoint.

        Note that this will start a webserver if captcha is
        triggered and `geetest_solver` is not passed.

        Raises
        ------
        - AccountLoginFail: Invalid password provided.
        - AccountDoesNotExist: Invalid email/username.
        """
        pass

    @base.region_specific(types.Region.CHINESE)
    async def cn_login_with_password(
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = False,
        port: int = 5000,
        geetest_solver: typing.Optional[typing.Callable[[SessionMMT], typing.Awaitable[SessionMMTResult]]] = None,
    ) -> CNWebLoginResult:
        """Login with a password via Miyoushe loginByPassword endpoint.

        Note that this will start a webserver if captcha is
        triggered and `geetest_solver` is not passed.
        """
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def check_mobile_number_validity(self, mobile: str) -> bool:
        """Check if a mobile number is valid (it's registered on Miyoushe).

        Returns True if the mobile number is valid, False otherwise.
        """
        pass

    @base.region_specific(types.Region.CHINESE)
    async def login_with_mobile_number(
        self,
        mobile: str,
        *,
        encrypted: bool = False,
        port: int = 5000,
    ) -> MobileLoginResult:
        """Login with mobile number, returns cookies.

        Only works for Chinese region (Miyoushe) users, do not include
        area code (+86) in the mobile number.

        Steps:
        1. Sends OTP to the provided mobile number.
        2. If captcha is triggered, prompts the user to solve it.
        3. Lets user enter the OTP.
        4. Logs in with the OTP.
        5. Returns cookies.
        """
        pass

    @base.region_specific(types.Region.OVERSEAS)
    async def login_with_app_password(
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = False,
        port: int = 5000,
        geetest_solver: typing.Optional[types.AppGeetestSolver] = None,
        device_id: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        device_name: typing.Optional[str] = None,
    ) -> AppLoginResult:
        """Login with a password via HoYoLab app endpoint.

        Note that this will start a webserver if captcha is
        triggered and ``geetest_solver`` is not passed.

        If email verification is triggered (can happen on first
        login with a new device), the verification code will be
        requested via CLI input.

        Raises
        ------
        - AccountLoginFail: Invalid password provided.
        - AccountDoesNotExist: Invalid email/username.
        - VerificationCodeRateLimited: Too many verification code requests.
        """
        pass

    @base.region_specific(types.Region.CHINESE)
    async def login_with_qrcode(self) -> QRLoginResult:
        """Login with QR code, only available for Miyoushe users."""
        pass

    @managers.no_multi
    async def create_mmt(self) -> MMT:
        """Create a geetest challenge."""
        pass

    @base.region_specific(types.Region.OVERSEAS)
    @managers.no_multi
    async def verify_mmt(self, mmt_result: MMTResult) -> None:
        """Verify a geetest challenge."""
        pass

    async def os_game_login(
        self,
        account: str,
        password: str,
        *,
        encrypted: bool = False,
        port: int = 5000,
        geetest_solver: typing.Optional[typing.Callable[[RiskyCheckMMT], typing.Awaitable[RiskyCheckMMTResult]]] = None,
    ) -> GameLoginResult:
        """Perform a login to the game.

        Raises
        ------
        - IncorrectGameAccount: Invalid account provided.
        - IncorrectGamePassword: Invalid password provided.
        """
        pass

    def _gen_random_fp(self) -> str:
        """Generate a random device fingerprint used for generating authentic device fingerprint."""
        pass

    def _gen_ext_fields(self, oaid: str, board: str) -> str:
        pass

    async def generate_fp(
        self,
        *,
        device_id: str,
        device_board: str,
        oaid: str,
    ) -> str:
        """Generate an authentic device fingerprint."""
        pass
