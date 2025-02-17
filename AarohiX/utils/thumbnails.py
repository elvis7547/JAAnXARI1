import os
import re
import textwrap

import aiofiles
import aiohttp
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

from AarohiX import app
from config import YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_thumb(videoid, user_id):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        try:
            wxy = await app.download_media(
                (await app.get_users(user_id)).photo.big_file_id,
                file_name=f"{user_id}.jpg",
            )
        except:
            wxy = await app.download_media(
                (await app.get_users(app.id)).photo.big_file_id,
                file_name=f"{app.id}.jpg",
            )

        xy = Image.open(wxy)
        a = Image.new("L", [640, 640], 0)
        b = ImageDraw.Draw(a)
        b.pieslice([(0, 0), (640, 640)], 0, 360, fill=255, outline="white")
        c = np.array(xy)
        d = np.array(a)
        e = np.dstack((c, d))
        f = Image.fromarray(e)
        x = f.resize((180, 180))

        youtube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(10))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.8)
        background.paste(x, (1065, 255), mask=x)

        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("AarohiX/assets/font2.ttf", 40)
        font2 = ImageFont.truetype("AarohiX/assets/font2.ttf", 30)
        arial = ImageFont.truetype("AarohiX/assets/font2.ttf", 35)
        name_font = ImageFont.truetype("AarohiX/assets/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (50, 600),
            f"{title[:30]}",
            fill="white",
            stroke_fill="white",
            font=font,
        )

        draw.text(
            (50, 565),
            f"{channel} | {views[:23]}",
            (255, 255, 255),
            font=arial,
        )

        draw.text(
            (50, 640),
            f"00:00",
            (255, 255, 255),
            stroke_width=1,
            stroke_fill="white",
            font=font2,
        )

        draw.text(
            (1150, 640),
            f"{duration[:23]}",
            (255, 255, 255),
            stroke_width=1,
            stroke_fill="white",
            font=font2,
        )

        draw.line((150, 660, 1130, 660), width=6, fill="white")
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass

        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL
