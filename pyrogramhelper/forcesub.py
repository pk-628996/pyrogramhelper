from pyrogram import enums
from pyrogram.errors import FloodWait, MessageNotModified,UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, Update

chat_to_search_member_in="i"
def chat_changer_forcesub(u):
   chat_to_search_member_in=u

async def checker(cl,msg):
  try:
    mem=await cl.get_chat_member(chat_to_search_member_in,msg.from_user.id)
  except UserNotParticipant:
    mem=False
  if mem:
    pass
  else:
    await msg.reply("You need to join https://t.me/link_shtrner_supp to use me",
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Now",url="https://t.me/link_shtrner_supp")]])
           )
    msg.stop_propagation()
