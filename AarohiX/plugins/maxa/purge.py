from pyrogram import Client, filters
import time
from AarohiX import app

async def purge_messages(client, message):
    start = time.perf_counter()
    
    if message.from_user is None:
        return
    
    if not await user_is_admin(client, user_id=message.from_user.id, message=message) and message.from_user.id not in [1087968824]:
        await message.reply("Sorry ʙᴜᴛ ᴀᴘ ɪꜱᴋᴇ ʟᴀʏᴀᴋ ɴʜɪ ʜᴏ. 🛑")
        return
    
    if not await can_delete_messages(client, message=message):
        await message.reply("ᴏᴏᴘꜱ! ɪ ᴄᴀɴ'ᴛ ꜱᴇᴇᴍ ᴛᴏ ᴘᴜʀɢᴇ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ʀɪɢʜᴛ ɴᴏᴡ 😔")
        return
    
    reply_msg = await message.get_reply_message()
    if not reply_msg:
        await message.reply("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴇʟᴇᴄᴛ ᴡʜᴇʀᴇ ᴛᴏ ꜱᴛᴀʀᴛ ᴘᴜʀɢɪɴɢ ꜰʀᴏᴍ.🔄")
        return
    
    messages = []
    message_id = reply_msg.message_id
    delete_to = message.message_id
    
    messages.append(message.reply_to_message.message_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await client.delete_messages(message.chat.id, messages)
            messages = []
    
    try:
        await client.delete_messages(message.chat.id, messages)
    except:
        pass
    
    # Delete the command message
    await message.delete()
    
    time_ = time.perf_counter() - start
    text = f"Purged Successfully in {time_:0.2f} Second(s). Operation completed swiftly! 😎"
    await message.reply(text, parse_mode="markdown")

async def delete_messages(client, message):
    if message.from_user is None:
        return
    
    if not await user_is_admin(client, user_id=message.from_user.id, message=message) and message.from_user.id not in [1087968824]:
        await message.reply("Sᴏʀʀʏ ʙᴜᴛ ᴀᴘ ɪꜱᴋᴇ ʟᴀʏᴀᴋ ɴʜɪ ʜᴏ. 🛑")
        return
    
    reply_msg = await message.get_reply_message()
    if not reply_msg:
        await message.reply("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛʜᴇ ᴍᴀꜱꜱᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ🔴")
        return
    
    del_message = [reply_msg.message_id, message.message_id]
    await client.delete_messages(message.chat.id, del_message)
    
    # Delete the command message
    await message.delete()

async def user_is_admin(client, user_id, message):
    # Your implementation to check if the user is an admin
    pass

async def can_delete_messages(client, message):
    # Your implementation to check if the bot can delete messages
    pass

app.on_message(filters.command("purge") & filters.group, purge_messages)
app.on_message(filters.command("del") & filters.group, delete_messages)
