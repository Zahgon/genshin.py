"""CLI tools."""

import asyncio
import datetime
import functools
import http.cookies
import os
import typing

import click

import genshin
from genshin import types

if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # type: ignore


T = typing.TypeVar("T", bound=typing.Any)

cli: click.Group = click.Group("cli")


def asynchronous(func: typing.Callable[..., typing.Awaitable[typing.Any]]) -> typing.Callable[..., typing.Any]:
    """Make an asynchronous function runnable by click."""
    pass


def client_command(func: typing.Callable[..., typing.Awaitable[typing.Any]]) -> typing.Callable[..., typing.Any]:
    """Make a click command that uses a Client."""
    pass


@cli.command()
@client_command
async def accounts(client: genshin.Client) -> None:
    """Get all of your genshin accounts."""
    pass


genshin_group: click.Group = click.Group("genshin", help="Genshin-related commands.")
honkai_group: click.Group = click.Group("honkai", help="Honkai-related commands.")
starrail_group: click.Group = click.Group("starrail", help="StarRail-related commands.")
cli.add_command(genshin_group)
cli.add_command(honkai_group)
cli.add_command(starrail_group)


@honkai_group.command("stats")
@click.argument("uid", type=int)
@client_command
async def honkai_stats(client: genshin.Client, uid: int) -> None:
    """Show simple honkai statistics."""
    pass


@genshin_group.command("stats")
@click.argument("uid", type=int)
@client_command
async def genshin_stats(client: genshin.Client, uid: int) -> None:
    """Show simple genshin statistics."""
    pass


@genshin_group.command("characters")
@click.argument("uid", type=int)
@client_command
async def genshin_characters(client: genshin.Client, uid: int) -> None:
    """Show genshin characters."""
    pass


@genshin_group.command("notes")
@click.argument("uid", type=int, default=None, required=False)
@client_command
async def genshin_notes(client: genshin.Client, uid: typing.Optional[int]) -> None:
    """Show real-Time notes."""
    pass


@starrail_group.command("notes")
@click.argument("uid", type=int, default=None, required=False)
@client_command
async def starrail_notes(client: genshin.Client, uid: typing.Optional[int]) -> None:
    """Show real-Time starrail notes."""
    pass


@cli.command()
@click.option("--scenario", help="Scenario ID or name to use (eg '12-3').", type=str, default=None)
@client_command
async def lineups(client: genshin.Client, scenario: typing.Optional[str]) -> None:
    """Show popular genshin lineups."""
    pass


@cli.command()
@click.option("--limit", help="The maximum amount of wishes to show.", type=int, default=None)
@client_command
async def wishes(client: genshin.Client, limit: typing.Optional[int] = None) -> None:
    """Show a nicely formatted wish history."""
    pass


@cli.command()
@client_command
async def pity(client: genshin.Client) -> None:
    """Calculate the amount of pulls until pity."""
    pass


@cli.command(hidden=True)
@client_command
async def banner_ids(client: genshin.Client) -> None:
    """Get the banner ids from logs."""
    pass


@cli.command(hidden=True)
def authkey() -> None:
    """Get an authkey from logfiles."""
    pass


@cli.command()
@click.option("-a", "--account", default=None, prompt=True)
@click.option("-p", "--password", default=None, prompt=True, hide_input=True)
@click.option("--port", help="Webserver port.", type=int, default=5000)
@asynchronous
async def login(account: str, password: str, port: int) -> None:
    """Login with a password."""
    pass


if __name__ == "__main__":
    cli()
