"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/b7753b6dc5498588eed5d.jpg"
pm_caption = "`CAGE X IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **1.15.0**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**CAGE DATABASE OS** : `3.0`\n"
pm_caption += "**Current Sat** : `Xzenderxus-2.25`\n"
pm_caption += f"**My Master** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `Hackersway Database 1.3.2 - Working Properly`\n\n"
pm_caption += "Rights Reserved : By [Xzͥenͣdͫer Cage](t.me/xzendercage)\n"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def USERX(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
