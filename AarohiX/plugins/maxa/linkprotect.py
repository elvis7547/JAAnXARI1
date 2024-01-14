from pyrogram import Client, filters
from AarohiX import app 

@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_links(client, message):
    if any(link in message.text for link in ["http", "https", "www."]):
        await message.delete()
      
@app.on_message(filters.group & filters.text & filters.regex(r'https?://[^\s]+'))
async def delete_links(client, message):
    await client.delete_messages(message.chat.id, message.message_id)
