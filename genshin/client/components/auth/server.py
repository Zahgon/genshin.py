"""Aiohttp webserver used for captcha solving."""

from __future__ import annotations

import asyncio
import typing
import webbrowser

import aiohttp
from aiohttp import web

from genshin import types
from genshin.models.auth.geetest import (
    MMT,
    MMTResult,
    MMTv4,
    MMTv4Result,
    RiskyCheckMMT,
    RiskyCheckMMTResult,
    SessionMMT,
    SessionMMTResult,
    SessionMMTv4,
    SessionMMTv4Result,
)
from genshin.utility import auth as auth_utility

__all__ = ["CAPTCHA_PAGE", "HOYOLAB_GT_SERVER", "enter_code", "launch_webapp", "solve_geetest"]

CAPTCHA_PAGE: typing.Final[str] = """
    <!DOCTYPE html>
    <head>
      <meta name="referrer" content="no-referrer"/>
    </head>
    <html>
      <body></body>
      <script src="./gt/v{gt_version}.js"></script>
      <script>
        const forNewOsApp = {for_new_os_app};
        const geetestVersion = {gt_version};
        const initGeetest = geetestVersion === 3 ? window.initGeetest : window.initGeetest4;
        fetch("/mmt")
          .then((response) => response.json())
          .then((mmt) => {
            const initParams = geetestVersion === 3 ? {
              gt: mmt.gt,
              challenge: mmt.challenge,
              new_captcha: mmt.new_captcha,
              api_server: "{api_server}",
              https: /^https/i.test(window.location.protocol),
              product: "bind",
              lang: "{lang}",
            } : {
              captchaId: mmt.captcha_id ?? mmt.gt,
              riskType: mmt.risk_type,
              userInfo: mmt.session_id ? JSON.stringify(forNewOsApp ? {
                session_id: mmt.session_id
              } : {
                mmt_key: mmt.session_id
              }) : undefined,
              apiServers: ["{api_server}"],
              product: "bind",
              language: "{lang}",
            };
            console.log(initParams);
            initGeetest(
              initParams,
              (captcha) => {
                captcha.onReady(() => {
                  geetestVersion == 3 ? captcha.verify() : captcha.showCaptcha();
                });
                captcha.onSuccess(() => {
                  fetch("/send-data", {
                    method: "POST",
                    body: JSON.stringify({
                      ...(mmt.session_id && {session_id: mmt.session_id}),
                      ...(mmt.check_id && {check_id: mmt.check_id}),
                      ...captcha.getValidate()
                    }),
                  });
                  document.body.innerHTML = "You may now close this window.";
                });
              }
            )
          });
      </script>
    </html>
    """


GT_V3_URL = "https://static.geetest.com/static/js/gt.0.5.0.js"
GT_V4_URL = "https://static.geetest.com/v4/gt4.js"
HOYOLAB_GT_SERVER = "gcaptcha4.captchami.com"


@typing.overload
async def launch_webapp(
    mmt: RiskyCheckMMT,
    *,
    lang: str = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> RiskyCheckMMTResult: ...
@typing.overload
async def launch_webapp(
    mmt: SessionMMT,
    *,
    lang: str = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> SessionMMTResult: ...
@typing.overload
async def launch_webapp(
    mmt: SessionMMTv4,
    *,
    lang: str = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> SessionMMTv4Result: ...
@typing.overload
async def launch_webapp(
    mmt: MMT,
    *,
    lang: str = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> MMTResult: ...
@typing.overload
async def launch_webapp(
    mmt: MMTv4,
    *,
    lang: str = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> MMTv4Result: ...
async def launch_webapp(
    mmt: typing.Union[MMT, MMTv4, SessionMMT, SessionMMTv4, RiskyCheckMMT],
    *,
    lang: typing.Optional[str] = None,
    api_server: typing.Optional[str] = None,
    for_new_os_app: typing.Optional[bool] = None,
    port: int = 5000,
) -> typing.Union[MMTResult, MMTv4Result, SessionMMTResult, SessionMMTv4Result, RiskyCheckMMTResult]:
    """Create and run a webapp to solve a geetest captcha."""
    pass


@typing.overload
async def solve_geetest(
    mmt: RiskyCheckMMT,
    *,
    lang: types.Lang = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> RiskyCheckMMTResult: ...
@typing.overload
async def solve_geetest(
    mmt: SessionMMT,
    *,
    lang: types.Lang = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> SessionMMTResult: ...
@typing.overload
async def solve_geetest(
    mmt: MMT,
    *,
    lang: types.Lang = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> MMTResult: ...
@typing.overload
async def solve_geetest(
    mmt: SessionMMTv4,
    *,
    lang: types.Lang = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> SessionMMTv4Result: ...
@typing.overload
async def solve_geetest(
    mmt: MMTv4,
    *,
    lang: types.Lang = ...,
    api_server: str = ...,
    for_new_os_app: bool = ...,
    port: int = ...,
) -> MMTv4Result: ...
async def solve_geetest(
    mmt: typing.Union[MMT, MMTv4, SessionMMT, SessionMMTv4, RiskyCheckMMT],
    *,
    lang: types.Lang = "en-us",
    api_server: str = "api-na.geetest.com",
    for_new_os_app: bool = False,
    port: int = 5000,
) -> typing.Union[MMTResult, MMTv4Result, SessionMMTResult, SessionMMTv4Result, RiskyCheckMMTResult]:
    """Start a web server and manually solve geetest captcha."""
    pass


async def enter_code(*, prompt: str = "Enter the verification code: ") -> str:
    """Get email or phone number verification code from the user via CLI input."""
    pass
