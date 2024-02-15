from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app
from config import OWNER_ID



@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("❤️‍🔥ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ❤️‍🔥")


@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("🥺ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ🥺")


@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"{message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} 💞")
           except:
             pass


@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)


@app.on_message(filters.command(["spg"], ["/", "!", "."]))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            result = ""
            
            if not response.get("items"):
                return await msg.edit("No results found!")
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("▶️Next▶️", data=f"next {start+10} {event.text.split()[1]}")]
            await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()

@app.on_message()
async def handle_message(client, message):
    # Handle other types of messages if necessary
    pass

@app.on_raw_update()
async def handle_raw_updates(client, update):
    if isinstance(update, types.UpdateGroupCall):
        if isinstance(update.call, types.GroupCallDiscarded):
            chat_id = update.chat_id
            user_id = update.call.user_id
            first_name = update.call.title
            mention = f"[{first_name}](tg://user?id={user_id})"
            await client.send_message(chat_id, f"{mention} ended the voice chat.")
