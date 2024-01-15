from AarohiX import app
from pyrogram import filters

@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_links(client, message):
    if any(link in message.text for link in ["http", "https", "www."]):
        custom_url = None
        for url in message.entities:
            if url.type == "url":
                custom_url = message.text[url.offset:url.offset + url.length]
        if custom_url and "https://youtu.be/" not in custom_url:
            # Your modified code goes here
            # Use 'custom_url' to remove the association between the song and the custom URL
            pass  # Placeholder, replace with your code
        else:
            await message.delete()
