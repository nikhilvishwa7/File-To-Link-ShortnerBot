import re
import aiohttp
import os
from os import environ
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

START_TXT = """
This is Permanent File Store Bot!
Send me any file I will save it in my Database. 
In return I give you a shortner url for accessing the file. 

📝 **Language:** [Python3](https://www.python.org)
📚 **Library:** [Pyrogram](https://docs.pyrogram.org)
📡 **Hosted on:** [Heroku](https://heroku.com)
🧑🏻‍💻 **Developer:** @WTF_BLAZE
👥 **Support Group:** [Deadly Support](https://t.me/theDeadlyBots)
📢 **Updates Channel:** [Deadly Channel](https://t.me/TheBotUpdates)
"""

Bot = Client(
    name=config.BOT_TOKEN,
    in_memory=True,
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH
)



@Bot.on_message(filters.private)
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)

@Bot.on_message((filters.document | filters.video | filters.audio & filters.private))
async def main(bot: Client, message: Message):
   reply = await message.reply_text("**Processing...**") 
   if message.from_user.id in config.BANNED_USERS:
       text_ok = await reply.edit("**YOUR ARE BANNED**\n\nPlease contact bot support for more information",
                                 disable_web_page_preview=True)
       return
   try:
      send_msg = await message.forward(config.CHANNEL_ID)
      file_id = str(send_msg.message_id) 
      file_link = f"https://t.me/{config.BOT_USERNAME}?start=shortner_{file_id}"
      print(file_link)
      text_ok = await reply.edit(f"your file stored successfully to our database here is your url\n {file_link}") 
   except Exception as err:
      text_op = await reply.edit("f**ERROR**\n\n{err}\n\n**SEND ASAP TO SUPPORT FOR FIXES**") 



@Bot.on_message(filters.command("start") & filters.private)
async def start(bot: Client, m: Message):
   if m.from_user.id in config.BANNED_USERS:
       await message.reply_text("**YOUR ARE BANNED**\n\nPlease contact bot support for more information",
                                 disable_web_page_preview=True)

Bot.start() 
