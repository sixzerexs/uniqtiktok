from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, html, F

import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"Hello, {message.from_user.full_name}!", reply_markup=kb.main)
    
@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer("UniqBot is bot for tik tok video uniqalazator")
    
@router.message()
async def cmd(message: Message):
    print(f'\"{message.text}\" from user - {message.from_user.username}')