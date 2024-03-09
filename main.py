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

# Инициализация бота с указанным токеном и режимом разбора HTML
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

# Основная асинхронная функция для запуска бота
async def main():
    # Настройка уровня логирования
    logging.basicConfig(level=logging.INFO)
    
    # Инициализация диспетчера для обработки обновлений от Telegram
    dp = Dispatcher()
    
    # Подключение маршрутизаторов для обработки команд бота
    dp.include_router(bot_start.router)
    # dp.include_router(bot_logic.router)
    # dp.include_router(bot_photo_load.router)
    dp.include_router(bot_stat.router)
    
    # Удаление веб-хука бота и запуск его в режиме опроса
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Точка входа в приложение
if __name__ == "__main__":
    # Запуск асинхронной функции main с использованием asyncio
    asyncio.run(main())
