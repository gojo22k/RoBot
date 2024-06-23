# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚","login🔑","DC"],
                ["follow❤️","ping📡","status📊","maintainers😎"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚","DC"],
                ["follow❤️","ping📡","status📊","maintainers😎"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('start⚡️')) & filters.private )
async def start(b, m):
    try:
        if not await db.is_user_exist(m.from_user.id):
            await db.add_user(m.from_user.id)
            await b.send_message(
                Var.BIN_CHANNEL,
                f"**New User Joined:** \n\n__Welcome__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __to your Bot !!__"
            )
        if Var.UPDATES_CHANNEL != "https://t.me/aniflixClou":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Sorry, You are Banned from using me. Contact the Developer__\n\n  **He will help you**",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await StreamBot.send_photo(
                    chat_id=m.chat.id,
                    photo="https://graph.org/file/9c910cbc74144b3b2efce.jpg",
                    caption="<i>Join CHANNEL to Use me🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Now 🔓", url=f"https://t.me/aniflixClou")
                            ]
                        ]
                    ),
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Something went wrong</i> <b> <a href='https://t.me/aniflixClou'>CLICK HERE FOR SUPPORT </a></b>",
                    disable_web_page_preview=True)
                return
        await StreamBot.send_photo(
            chat_id=m.chat.id,
            photo ="https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg",
            caption =f'Hi {m.from_user.mention(style="md")}!,\nI am Telegram File to Link Generator Bot with Channel support.\nSend me any file and get a direct download link and streamable link.!',
            reply_markup=buttonz)
    
    except Exception as e:
        if "[400 CHAT_ADMIN_REQUIRED]" in str(e):
            await b.send_message(
                chat_id=m.chat.id,
                text="Error: The bot does not have sufficient admin rights in the channel.",
                disable_web_page_preview=True
            )
        else:
            await b.send_message(
                chat_id=m.chat.id,
                text=f"Something went wrong: {e}",
                disable_web_page_preview=True
            )

@StreamBot.on_message((filters.command("help") | filters.regex('help📚')) & filters.private )
async def help_handler(bot, message):
    try:
        if not await db.is_user_exist(message.from_user.id):
            await db.add_user(message.from_user.id)
            await bot.send_message(
                Var.BIN_CHANNEL,
                f"**New User Joined **\n\n__Welcome__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __to your Bot !!__"
            )
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=message.chat.id,
                        text="<i>Sorry Sir, You are Banned From Using me. Contact the Developer</i>",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await StreamBot.send_photo(
                    chat_id=message.chat.id,
                    photo="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
                    Caption="**Join SUPPORT GROUP TO USE this Bot!**\n\n__Due to Overload, Only Channel Subscribers can use the Bot!__",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                )
                return
            except Exception:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="__Something went Wrong. Contact me__ [ANIFLIX](https://t.me/aniflixClou).",
                    disable_web_page_preview=True)
                return
        await message.reply_text(
            text="""<b> Send me any file or video i will give you streamable link and download link.</b>\n
<b> I also support Channels, add me to you Channel and send any media files and see miracle✨ also send /list to know all commands""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("💁‍♂️ DEV", url="https://t.me/aniflixClou")],
                    [InlineKeyboardButton("💥 Source Code", url="https://t.me/aniflixClou")]
                ]
            )
        )
    
    except Exception as e:
        if "[400 CHAT_ADMIN_REQUIRED]" in str(e):
            await bot.send_message(
                chat_id=message.chat.id,
                text="Error: The bot does not have sufficient admin rights in the channel.",
                disable_web_page_preview=True
            )
        else:
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"Something went wrong: {e}",
                disable_web_page_preview=True
            )
