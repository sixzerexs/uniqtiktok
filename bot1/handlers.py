import requests
import os
import io
import secrets
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram import Router
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

URI_PHOTO_INFO = f"https://api.telegram.org/bot{TOKEN}/getfile?file_id="
URI_PHOTO_PATH = f"https://api.telegram.org/file/bot{TOKEN}/"

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message): #not a bigger than 10mgb and 10000x10000
    await message.reply(f"Hello, @{message.from_user.username}! Just send a photo if you want to make it unique.\n\nCommands:\n1. /start\n2. /info\n\n*the bot may be delayed @uniqtbot")
    
@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer(f"UniqBot is bot for tiktok video uniqalazator \n\nHow it use?\n1. Send me the image you want to make unique.\n2. Save the image the bot sent you\n3. Use\n\n@uniqtbot")

@router.message()
async def cmd(message: Message):
    if message.photo:
        msg_temp = await message.answer("Photo at proccesing...")
        img_name = secrets.token_hex(8)
        img_text = message.caption
        
        print(message.caption)
        
        lastElement = len(message.photo) - 1
        fileid = message.photo[lastElement].file_id
        resp = requests.get(URI_PHOTO_INFO + fileid)
        img_uri_path = resp.json()['result']['file_path']
        img = requests.get(URI_PHOTO_PATH + img_uri_path)
        img = Image.open(io.BytesIO(img.content))
        
        img = ImageEnhance.Brightness(img).enhance(1.13)
        img = ImageEnhance.Contrast(img).enhance(1.1)
        img = ImageEnhance.Color(img).enhance(0.85)
        # img = ImageEnhance.Sharpness(img).enhance(1.12)
        img = img.filter(ImageFilter.SHARPEN)
        
        width, height = img.size
        img = img.crop((10,10,width-10,height-10))
        
        d = ImageDraw.Draw(img)
        d.line((0, height, width, 0), fill=0)
        
        fnt = ImageFont.truetype("bot1/fonts/Arco.ttf", 20)#img text take from caption img
        _, _, w, h = d.textbbox((0, 0), img_text, font=fnt)
        d.text(((width-w)/2, height-height/100*10), f"{img_text}", font=fnt, fill=(230,230,230))#xy = inline_keyboard(center,left,right....)
        
        if not os.path.exists('bot1/static'):
            os.mkdir('bot1/static')
        img.save(f'bot1/static/{img_name}.png', format='PNG')
        await msg_temp.delete()
        await message.answer_photo(photo=FSInputFile(f'bot1/static/{img_name}.png'), caption=f'@{message.from_user.username} image.\n\n@uniqtbot')
    else:
        print(f'\"{message.text}\" from user - {message.from_user.id}')