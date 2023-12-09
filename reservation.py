import re

from aiogram import Bot, Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config_reader import config
from main_buttons.buttons import main_kb, book_kb, rmk
from utils.states import Form


reservation_router = Router()
bot = Bot(token=config.bot_token.get_secret_value())

@reservation_router.message(StateFilter(None), F.text.lower() == '🤳забронировать стол')
async def booking(message: types.Message, state: FSMContext):
    await message.answer('👥Укажите ваш номер телефона:', reply_markup=rmk)
    await state.set_state(Form.phone)

@reservation_router.message(Form.phone)
async def phone(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(phone=message.text)
        await state.set_state(Form.name)
        await message.answer('👤Укажите ваше имя:')
    else:
        await message.answer(
            '❌Поле заполнены не верно.❌\n\n'
            'Введите номер цифрами.',
            reply_markup=main_kb()
        )
        await state.clear()

@reservation_router.message(Form.name)
async def name(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(name=message.text)
        await state.set_state(Form.date_time)
        await message.answer('📅Укажите дату и время бронирования:')
    else:
        await message.answer(
            '❌Поле заполнены не верно.❌\n\n'
            'Введите свое имя.',
            reply_markup=main_kb()
        )
        await state.clear()

@reservation_router.message(Form.date_time)
async def date_time(message: types.Message, state: FSMContext):
    if re.match(r'^[\d\W]+$', message.text):
        await state.update_data(date_time=message.text)
        data = await state.get_data()
        await message.answer(
            f'Вы хотите забронировать стол на {data["date_time"]}?\n\n'
            f'Ваше имя: {data["name"]}\n'
            f'Ваш номер телефона: {data["phone"]}\n\n',
            reply_markup=book_kb()
        )
        await state.set_state()
    else:
        await message.answer(
            '❌Поле заполнены не верно.❌\n\n'
            'Используйте цифры и знаки препинания.',
            reply_markup=main_kb()
        )
        await state.clear()

@reservation_router.message(StateFilter(None), F.text.lower() == '✅да')
async def yes_booking(message: Message, state: FSMContext):
    data = await state.get_data()
    phone = data.get('phone')
    name = data.get('name')
    date_time = data.get('date_time')
    if phone is not None and name is not None and date_time is not None:
        admin_channel_id = config.admin_channel_id.get_secret_value()
        admin_message = (
            f'‼️НОВОЕ БРОНИРОВАНИЕ:‼️\n\n'
            f'Телефон: {phone}\n'
            f'Имя: {name}\n'
            f'Дата и время: {date_time}\n\n'
            f'От пользователя: @{message.from_user.username} (ID: {message.from_user.id})'
        )
        await bot.send_message(admin_channel_id, admin_message)
        await message.answer(
            '✅Ваше бронирование успешно подтверждено.✅\n\n'
            'В ближайшее время с вами свяжется наш менеджер.\n\n'
            'Спасибо, что выбрали нас!😊',
            reply_markup=main_kb()
        )
        await state.clear()
    else:
        error_message = (
            '❌Поля заполнены не верно.❌\n\n'
            'Пожалуйста, попробуйте еще раз.'
        )
        await message.answer(
            error_message,
            reply_markup=main_kb()
        )
        await state.clear()

@reservation_router.message(StateFilter(None), F.text.lower() == '❌нет')
async def no_booking(message: Message, state: FSMContext):
    await message.answer(
        '❌Ваше бронирование отменено.❌\n\n'
        'Вы вернулись в главное меню.',
        reply_markup=main_kb()
    )
    await state.clear()
