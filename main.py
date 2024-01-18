from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
from models import get_users, init, get_user, create_user
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message, ContentType
from config import BOT_TOKEN
from app.keyboards import main_kb, inspection_kb
from utilites.utilits_bot import coincidence
# import bot_logic
import bot_start
# import bot_photo_load
import bot_stat

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    dp.include_router(bot_start.router)
    # dp.include_router(bot_logic.router)
    # dp.include_router(bot_photo_load.router)
    dp.include_router(bot_stat.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())