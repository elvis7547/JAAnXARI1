import os
from pyrogram import Client
from AarohiX import app 

ASSISTANT_USERNAME = "ari_assistant_mx"

async def on_chat_member(client, update):
    if update.new_chat_member is not None and update.new_chat_member.username == ASSISTANT_USERNAME:
        try:
            chat = await client.get_chat(update.chat.id)
            await client.kick_chat_member(chat.id, ASSISTANT_USERNAME)
        except Exception as e:
            print(f"Error removing assistant from group: {e}")

app.add_handler(on_chat_member)
