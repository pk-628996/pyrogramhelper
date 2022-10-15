from pyrogram import enums
import pyrogram
from pyrogram.errors import FloodWait, MessageNotModified,UserNotParticipant
from pytube import *
from asyncio.subprocess import PIPE as asyncPIPE
from pyrogram import Client,filters
from asyncio import create_subprocess_shell as asyncrunapp
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, Update
import asyncio,json,math,os,subprocess,time,humanize,shutil,json,requests
from datetime import datetime
from aiohttp import ClientSession
from aiofiles import open as openfile
from .media_func import *
from .progress import *
from convopyro import listen_message
import random

class sender():
 """Just a simple class to store functions"""
 async def sendVideo(msg,file,thumb=None):
   duration=durationfunc(f"""{file}""")
   up=await msg.reply("Uploading⚡..",quote=True)
   if thumb:   
     start=time.time()
     try:
       await msg.reply_video(f"""{file}""",quote=True,progress=progress,progress_args=(up,start,"Uploading⚡.."),caption=f"""{str(file).split("/")[-1]}""",thumb=thumb,duration=duration,width=320,height=180,supports_streaming=True)
     except:
         await up.edit("An error occurred")
     await up.delete()
     os.remove(f"""{file}""")
   else:
     start=time.time()
     try:
       await msg.reply_document(f"""{file}""",quote=True,progress=progress,progress_args=(up,start,"Uploading⚡.."),caption=f"""{str(file).split("/")[-1]}""")
     except:
        await up.edit("An error occurred")

 """Description:sendVideo,Usage:-
 await sendVideo(msg,your_file,thumb=your_thumbnail)
 or 
 await sendVideo(msg,your_file)
 thumbnail is optional 
 if thumbnail is not provided the videos will be uploaded in document format"""

 async def sendDocument(msg,file,thumb=None):
   up=await msg.reply("Uploading⚡..",quote=True)
   if thumb:   
     start=time.time()
     try:
       await msg.reply_document(f"""{file}""",quote=True,progress=progress,progress_args=(up,start,"Uploading⚡.."),caption=f"""{str(file).split("/")[-1]}""",thumb=thumb)
     except:
         await up.edit("An error occurred")
     await up.delete()
     os.remove(f"""{file}""")
   else:
     start=time.time()
     try:
       await msg.reply_document(f"""{file}""",quote=True,progress=progress,progress_args=(up,start,"Uploading⚡.."),caption=f"""{str(file).split("/")[-1]}""")
     except:
        await up.edit("An error occurred")

class downloader():
 """Just a simple class to store functions"""
 async def download_1_reply(msg):
   up=await msg.edit("Downloading⚡..")
   try:
    start=time.time()
    file=await msg.reply_to_message.download(progress=progress,progress_args=(up,start,"Downloading⚡.."))
    await up.delete()
    return f"""{file}"""
   except:
     await up.edit("An error Occurred")
     pass
