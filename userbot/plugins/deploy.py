"""Emoji

Available Commands:

.deploy"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

from userbot import AUTONAME


DEFAULTUSER = str(AUTONAME) if AUTONAME else "USERX"

@borg.on(admin_cmd(pattern=r"deploy"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

   # input_str = event.pattern_match.group(1)



    await event.edit("Deploying...")

    animation_chars = [
        
            "**Riot Connecting To Latest Github Build (xzendercage/cageuserx)**",
            "**Build started by user** **{DEFAULTUSER}**",
            "**Deploy** `535a74f0` **by user** **{DEFAULTUSER}**",
            "**Restarting Riot Server...**",
            "**State changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m stdborg`",
            "**State changed from starting to up**",
            "__INFO:USERX:Logged in as 557667062__",
            "__INFO:USERX:Successfully loaded all plugins__",
            "**Build Succeeded**"

 ]

    for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
