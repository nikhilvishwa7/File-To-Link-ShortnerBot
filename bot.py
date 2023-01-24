
import os
import asyncio
import traceback
from binascii import (
    Error
)
from pyrogram import (
    Client,
    filters
)
from pyrogram.errors import (
    UserNotParticipant,
    FloodWait,
    QueryIdInvalid
)
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
import config



# API_KEY
# SHORTNER_SITE

@Bot.on_message((filters.document | filters.video | filters.audio & filters.private))
async def main(bot: Client, message: Message):
   reply = await message.reply_text("**Processing...**") 
   if message.from_user.id in Config.BANNED_USERS:
       await message.reply_text("**YOUR ARE BANNED**\n\nPlease contact bot support for more information",
                                 disable_web_page_preview=True)
       return
   try:
      send_msg = await message.forward(config.DB_CHANNEL)
      file_id = str(send_msg.message_id) 
      file_link = f"https://t.me/{Config.BOT_USERNAME}?start=shortner_{file_id}"
      link_shortner = requests.get(f"{shortner_site}/api?api={api_key}&url={file_link}&alias=CustomAlias")
      text_ok = await reply.edit("your file stored successfully to our database here is your url", 
   except Exception as err:
      text_op = await reply.edit("f**ERROR**\n\n{err}\n\n**SEND ASAP TO SUPPORT FOR FIXES**") 
