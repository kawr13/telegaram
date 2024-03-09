# телеграм_бот.py
from aiogram import Bot, Dispatcher, types, F
import asyncio
import io
import logging
import datetime
from icecream import ic
from numpy import number
from models import get_users, init, get_user, create_user, create_conteiner, get_first_conteiner, ImagesConteiner, get_conteiner, StatusConteiner
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message, ContentType, InputMediaPhoto, InputFile
from config import BOT_TOKEN
from aiogram.fsm.context import FSMContext
from app.keyboards import main_kb, inspection_kb, completion, data_conteiner, start_kb
from utilites.utilits_bot import coincidence
from aiogram import Router
from form.forms import Form, Stat
import os
from random import randint

# Инициализация маршрутизатора для обработки сообщений бота
router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def start_message(message: Message):
    # Инициализация базы данных
    await init()
    # Проверка существования пользователя в базе данных
    user = await get_user(message.from_user.id)
    if not user:
        # Если пользователь не существует, создаем его с необходимыми данными
        username = message.from_user.username if message.from_user.username else 'Не указано'
        first_name = message.from_user.first_name if message.from_user.first_name else 'Не указано'
        last_name = message.from_user.last_name if message.from_user.last_name else 'Не указано'
        await create_user(username=username, usertelegram_id=message.from_user.id, first_name=first_name, last_name=last_name, password='')
    # Отправка сообщения с клавиатурой действий
    await message.reply(f'Выберете действие', reply_markup=main_kb)

# Обработчик команды /help
@router.message(Command(commands=['help']))
async def process_helper(message: Message):
    # Отправка сообщения с инструкциями по началу работы
    await message.reply('Напишите /start для начала работы')

# Пример обработчика, который не используется в вашем коде
# @router.message(F.text != 'Проверка заявок по контейнеру')
# async def canceling(message: Message):
#     messages = 'Выберите действие'
#     await message.reply(messages, reply_markup=main_kb)
