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
from app.keyboards import main_kb, inspection_kb, completion, data_conteiner, start_kb, canceling_kb
from utilites.utilits_bot import coincidence, data_cont, data_async_cont
from aiogram import Router
from form.forms import Form, Stat
from datetime import datetime
import os
from random import randint


router = Router()


@router.message(F.text == 'Проверка заявок по контейнеру')
async def data_status_conteiner(messege: Message, state: FSMContext):
    await state.set_state(Stat.conteiner)
    await messege.reply('Введите номер контейнера', reply_markup=ReplyKeyboardRemove())
    
@router.message(Stat.conteiner, F.text)
async def detecting(message: Message, state: FSMContext):
    option = False
    # if coincidence(message.text) and len(message.text) > 11:
    #     option = True
    #     date_start = message.text.split()[1]
    #     date_end = message.text.split()[2]
    if coincidence(message.text) and len(message.text) == 11:
        option = False
        cont_num = message.text.upper()
        data = await data_async_cont(cont_num)
        response_message = f'Контейнер: {data["result"][0]["ContNum"]}\n'
        for dat in data.get("result"):
            if dat['Status'] is False:
                print(dat)
                continue
            else:
                date_object_until = datetime.strptime(dat["Until"], "%Y-%m-%dT%H:%M:%S")
                date_object = datetime.strptime(dat["From"], "%Y-%m-%dT%H:%M:%S")
                formatted_date_from = date_object.strftime("%d.%m.%Y")
                formatted_date_until = date_object_until.strftime("%d.%m.%Y")
                response_message += (
                    # f"Срок действия:\n"
                    # f"{formatted_date_from} - {formatted_date_until}\n"  
                    f"начало действия заявки: 00:00 {formatted_date_from}\n"
                    f"окончание:   23:59 {formatted_date_until}\n"
                    # f"Статус: {dat['Status']}"
                )

        if len(response_message.split()) == 3:
            response_message += 'Нет заявок'
        await message.reply(response_message, reply_markup=canceling_kb)
        
    elif message.text == 'Завершить':
            messages = 'Выберите действие'
            await message.reply('/start', reply_markup=main_kb)
            await state.clear()
    else:
        messages = 'Номер введен некорректно'
        await message.reply(messages, reply_markup=canceling_kb)
        await state.set_data()

    

@router.message(Stat.conteiner, F.text == 'Завершить')
async def handle_photo(message: types.Message, state: FSMContext):
    # Обработка фото
    await message.reply('Выберете действие', reply_markup=main_kb)
    await state.clear()
