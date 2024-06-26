import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router

load_dotenv()
TOKEN = os.getenv('TOKEN')

dp = Dispatcher()

async def main():
    bot = Bot(token=TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print('Bot is turn off') 