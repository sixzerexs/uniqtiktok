import requests
import os
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from dotenv import load_dotenv

import keyboards as kb

load_dotenv()
TOKEN = os.getenv('TOKEN')

URI_PHOTO_INFO = f"https://api.telegram.org/bot{TOKEN}/getfile?file_id="
URI_PHOTO_PATH = f"https://api.telegram.org/file/bot{TOKEN}/"

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Hello, {message.from_user.full_name}!", reply_markup=kb.main)
    
@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer(f"UniqBot is bot for tik tok video uniqalazator \n\nHow it use? \n1. Select the command \"Uniquelize\"\n2. Send a img what u would to unique\n3. Save the image the bot sent you\n\n@uniqtbot")
    print(img_byte_code)
    
@router.message()
async def cmd(message: Message):
    if message.photo:
        global img_byte_code
        lastElement = len(message.photo) - 1
        fileid = message.photo[lastElement].file_id
        resp = requests.get(URI_PHOTO_INFO + fileid)
        img_path = resp.json()['result']['file_path']
        img_byte_code = (requests.get(URI_PHOTO_PATH + img_path)).content
    else:
        print(f'\"{message.text}\" from user - {message.from_user.username}')
        