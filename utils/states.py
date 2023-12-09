from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    phone1 = State()
    name1 = State()
    address = State()
    dishes = State()
    phone = State()
    name = State()
    date_time = State()
