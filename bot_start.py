# телеграм_бот.py
from ast import For
from calendar import c
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



router = Router()

@router.message(CommandStart())
async def echo_message(message: Message):
    # await init()  # Вызывайте функцию инициализации базы данных перед использованием моделей
    # if not await get_user(message.from_user.id):
    #     if message.from_user.username is None or message.from_user.first_name is None or message.from_user.last_name is None:
    #         username = 'Не указано'
    #         first_name = 'Не указано'
    #         last_name = 'Не указано'
    #     else:
    #         username = message.from_user.username
    #         first_name = message.from_user.first_name
    #         last_name = message.from_user.last_name
    #     await create_user(username=username, usertelegram_id=message.from_user.id, first_name=first_name, last_name=last_name, password='')
    # user = await get_user(message.from_user.id)
    await message.reply(f'Выберете действие', reply_markup=main_kb)

@router.message(Command(commands=['help']))
async def process_helper(message: Message):
    await message.reply('Напишите /start для начала работы')
    

# @router.message(F.text != 'Проверка заявок по контейнеру')
# async def canceling(message: Message):
#     messages = 'Выберите действие'
#     await message.reply(messages, reply_markup=main_kb)

    
