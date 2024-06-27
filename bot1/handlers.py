import requests
import os
import io
import secrets
from PIL import Image, ImageFilter, ImageEnhance
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
async def cmd_start(message: Message):
    await message.reply(f"Hello, @{message.from_user.username}! Just send a photo if you want to make it unique.\n\nCommands:\n1. /start\n2. /info\n\n*the bot may be delayed @uniqtbot")
    
@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer(f"UniqBot is bot for tiktok video uniqalazator \n\nHow it use?\n1. Send me the image you want to make unique.\n2. Save the image the bot sent you\n3. Use\n\n@uniqtbot")
    
@router.message()
async def cmd(message: Message):
    if message.photo:
        lastElement = len(message.photo) - 1
        fileid = message.photo[lastElement].file_id
        resp = requests.get(URI_PHOTO_INFO + fileid)
        img_uri_path = resp.json()['result']['file_path']
        img = requests.get(URI_PHOTO_PATH + img_uri_path)
        img = Image.open(io.BytesIO(img.content))
        img = img.filter(ImageFilter.GaussianBlur(radius=1.05))
        img = ImageEnhance.Brightness(img).enhance(1.1)
        img = ImageEnhance.Contrast(img).enhance(1.1)
        img = ImageEnhance.Color(img).enhance(1.05)
        img = ImageEnhance.Sharpness(img).enhance(1.1)
        if not os.path.exists('bot1/static'):
            os.mkdir('bot1/static')
        img_name = secrets.token_hex(8)
        img.save(f'bot1/static/{img_name}.png', format='PNG')
        await message.answer_photo(photo=FSInputFile(f'bot1/static/{img_name}.png'), caption='123')
    else:
        print(f'\"{message.text}\" from user - {message.from_user.id}')