from pyrogram.types import *
from pyrogram.errors import *
from config import *


async def forcesub(bot, update):
        try:
            await bot.get_chat_member(force_subchannel, update.from_user.id)
        except UserNotParticipant:
            file_id = "CAADBQADOAcAAn_zKVSDCLfrLpxnhAI"
            return await bot.send_sticker(update.chat.id, file_id)
            text = FORCESUB_TEXT
            reply_markup = FORCESUB_BUTTONS
            await bot.send_message(update.from_user.id,
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True) 
       
