import time,math
import os,subprocess
import requests,json
import asyncio
import humanize
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message,InlineKeyboardMarkup, InlineKeyboardButton


def ts(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]

def hbs(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "B", 1: "K", 2: "M", 3: "G", 4: "T", 5: "P"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"

async def progress(current, total, message,start, file=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        time_to_completion = round((total - current) / speed) * 1000
        progress_str = "{0}{1}** {2}%**\n\n".format(
            "".join(["🔹" for i in range(math.floor(percentage / 5))]),
            "".join(["□" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )
        tmp = (
            progress_str
            + "**✅ Progress:** {0} \n\n**📁 Total Size:** {1}\n\n**🚀 Speed:** {2}/s\n\n**⏰ Time Left:** {3}\n".format(
                hbs(current),
                hbs(total),
                hbs(speed),
                ts(time_to_completion),
            )
        )
        if file:
            await message.edit(
                "Status: {}\n\n{}".format(file, tmp)
            )
        else:
            await message.edit("{}".format(tmp))

def keyt(name,data):
 keyboard=InlineKeyboardButton(name,callback_data=data)
 return keyboard






