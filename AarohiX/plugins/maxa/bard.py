import pyrogram
from pyrogram import Client
from pyrogram import filters
from bardapi import Bard
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app

WELCOME_MSG = (
    "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ʙᴏᴛ! ɪ ᴀᴍ ᴀɪ ʙᴀꜱᴇᴅ ᴏɴ ɢᴏᴏɢʟᴇ ʙᴀʀᴅ.\n\n"
    "ᴛᴏ ɢᴇᴛ ꜱᴛᴀʀᴛᴇᴅ, ᴜꜱᴇ ʙᴇʟᴏᴡ ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ᴡᴏᴜʟᴅ ʟɪᴋᴇ ᴛᴏ ᴜꜱᴇ.\n\n"
    "ᴛᴏ ᴜꜱᴇ ɪᴛ ᴛʏᴘᴇ /ᴀꜱᴋ ᴀɴᴅ ᴡʀɪᴛᴇ ʏᴏᴜʀ ᴘʀᴏᴍᴘᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴛᴀʀᴛ ᴀɪ ᴄʜᴀᴛ.\n\n"
    "ᴇxᴀᴍᴘʟᴇ ᴜꜱᴀɢᴇ:\n\n"
    "/ask [Your Command]\n\n
    ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ <a href=\"https://t.me/lll_notookk_lll\">||ᴀʀɪ||❣️</a>"
)

DEMO_PHOTO = "https://telegra.ph/file/f9b2332612fad16e49b66.jpg" #--- Logo File name.
        
key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ Add Me to Group", url="https://t.me/botusername?startgroup")
                ]
            ]
)
            
@app.on_message(filters.command("ask", prefixes="/"))
def ask_command(client, message):
    query = " ".join(message.command[1:])
    response = bard.get_answer(query)['content']
    message.reply(response)
    
@app.on_message(filters.reply)
def message_command(client, message):
    if message.reply_to_message.from_user.id == YouUserId: #--- Enter User Id Here.
        response = bard.get_answer(message.text)['content']
        message.reply(response)
    
@app.on_message(filters.command("start"))
def start(bot, message):
    bot.send_photo(
        message.chat.id,
        DEMO_PHOTO,
        WELCOME_MSG,
        reply_markup=key,
    )
    
if name == "main":
    app.run()
