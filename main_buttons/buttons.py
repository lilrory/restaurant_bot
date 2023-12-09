from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder() 
    kb.button(text='📕Меню')
    kb.button(text='🚘Доставка')
    kb.button(text='🤳Забронировать стол')
    kb.button(text='🕓Режим работы')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def book_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder() 
    kb.button(text='✅Да')
    kb.button(text='❌Нет')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def delivery_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder() 
    kb.button(text='✅')
    kb.button(text='❌')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

rmk = ReplyKeyboardRemove()
