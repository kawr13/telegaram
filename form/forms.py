from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    number = State()
    photo = State()
    
    
class Stat(StatesGroup):
    conteiner = State()