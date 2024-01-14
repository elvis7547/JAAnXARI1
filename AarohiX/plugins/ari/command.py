from AarohiX import app
from pyrogram import Client, filters
from config import *

# Initialize the Pyrogram client
bot = Client("BOT_TOKEN")

# Define a common function for sending the jaan photo reply
async def send_jaan_photo(client, message):
    photo_file_path = "https://telegra.ph/file/fcfbda3f6f3390adc51c2.jpg"
    await message.reply_photo(photo=photo_file_path, caption="❤️‍🔥━━♡゙")

# Handle both /jaan and /jann commands
@app.on_message(filters.command(["command", "module", "extra"]))
async def handle_jaan_commands(client, message):
    await send_jaan_photo(client, message)
