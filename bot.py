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
      url_link = await get_shortlink(file_link)
      text_ok = await reply.edit(f"your file stored successfully to our database here is your url\n {url_link}") 
   except Exception as err:
      text_op = await reply.edit("f**ERROR**\n\n{err}\n\n**SEND ASAP TO SUPPORT FOR FIXES**") 



@Bot.on_message(filters.command("start") & filters.private)
async def start(bot: Client, m: Message):
   if m.from_user.id in config.BANNED_USERS:
       await message.reply_text("**YOUR ARE BANNED**\n\nPlease contact bot support for more information",
                                 disable_web_page_preview=True)
       return

       
    
    usr_cmd = cmd.text.split("_", 1)[-1]
    if usr_cmd == "/start":
        await m.reply_text(
            START_TXT.format(m.from_user.first_name, m.from_user.id),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Support Group", url=f"https://t.me/{cofig.SUPPORT_CHAT}"),
                        InlineKeyboardButton("Bots Channel", url=f"https://t.me/{config.SUPPORT_CHANNEL}")
                    ],                    
                ]
            )
        )
    else:
        try:
            try:
                file_id = int(usr_cmd).split("_")[-1])
            GetMessage = await bot.get_messages(chat_id=config.CHANNEL_ID, message_ids=file_id)
            message_ids = []
            if GetMessage.text:
                message_ids = GetMessage.text.split(" ")
                _response_msg = await cmd.reply_text(
                    text=f"**Total Files:** `{len(message_ids)}`",
                    quote=True,
                    disable_web_page_preview=True
                )
            else:
                message_ids.append(int(GetMessage.message_id))
            for i in range(len(message_ids)):
                await send_media_and_reply(bot, user_id=cmd.from_user.id, file_id=int(message_ids[i]))
        except Exception as err:
            text_op = await m.reply.text("f**ERROR**\n\n{err}\n\n**SEND ASAP TO SUPPORT FOR FIXES**") 

async def get_shortlink(file_link):
    url = "https://easysky.in/api?api=8644d61bb75d25519b6b0acdec99bf369fa1cbdd&url={file_link}"
    params = {'api': API_KEY, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

Bot.start() 
