import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Craxy import LOGGER, app, userbot
from Craxy.core.call import Crax
from Craxy.plugins import ALL_MODULES
from Craxy.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Craxy").error(
            "WTF DOST ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Craxy").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Craxy.plugins." + all_module)
    LOGGER("Craxy.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Crax.start()
    try:
        await Crax.stream_decall("https://te.legra.ph/file/af14da3e36cf327fd9247.mp4")
    except:
        pass
    try:
        await Crax.stream_call(
            "https://te.legra.ph/file/af14da3e36cf327fd9247.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Craxy").error(
            "[ERROR] - \n\nHey DOST, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Crax.decorators()
    LOGGER("Craxy").info("\x41\x6e\x6f\x6e\x58\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x2e\x2e\n\n\x4e\x6f\x77\x20\x64\x72\x6f\x70\x20\x79\x6f\x75\x72\x20\x67\x69\x72\x6c\x66\x72\x69\x65\x6e\x64\'\x73\x20\x6e\x75\x64\x65\x73\x20\x61\x74\x20\x40\x44\x65\x76\x69\x6c\x73\x48\x65\x61\x76\x65\x6e\x4d\x46")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Craxy").info("Stopping Music Bot...")
