from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Проверка заявок по контейнеру"),
            # KeyboardButton(text="Осмотр контейнера"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)

inspection_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ввести номер в ручную"),
            KeyboardButton(text="Сфотографировать номер контейнера"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)

canceling_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Завершить"),
            # KeyboardButton(text="Проверка заявок по контейнеру"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)

completion = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Готово"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)

data_conteiner = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Введите номер контейнера"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)