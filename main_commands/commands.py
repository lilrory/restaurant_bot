from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from main_buttons.buttons import main_kb
from reservation import booking, yes_booking, no_booking
from delivery import delivery, yes_delivery, no_delivery

router = Router()


@router.message(Command('start'))
async def start(message: Message):
    user_name = message.from_user.username
    await message.answer(
        f'Добро пожаловать в 🍕Pizza🍕, @{user_name}!\n'
        f'Снизу находятся кнопки управления ботом.\n',
        reply_markup=main_kb()
    )

@router.message(F.text.lower() == '🕓режим работы')
async def work_time(message: Message):
    await message.answer(
        f'Pizza🍕\n\n'
        f'Режим работы:\n'
        f'ПН-ВС: 10:00 - 22:30\n\n'
        f'Адрес: Астана\n\n'
        f'☎️Тел: +7 (777) 777-77-77\n',
        reply_markup=main_kb()   
    )

@router.message(F.text.lower() == '📕меню')
async def menu(message: Message):
    await message.answer(
        'Здесь вы можете ознакомиться с нашим меню.\n\n'
        'https://telegra.ph/Menyu-12-08-10',
        reply_markup=main_kb()   
    )    

# забронировать стол
@router.message(StateFilter(None), F.text.lower() == '🤳забронировать стол')
async def booking_handler(message: types.Message, state: FSMContext):
    await booking(message, state)

@router.message(StateFilter(None), F.text.lower() == '✅да')
async def yes_booking_handler(message: types.Message, state: FSMContext):
    await yes_booking(message, state)

@router.message(StateFilter(None), F.text.lower() == '❌нет')
async def no_booking_handler(message: types.Message, state: FSMContext):
    await no_booking(message, state)

# доставка
@router.message(StateFilter(None) ,F.text.lower() == '🚘доставка')
async def delivery_handler(message: types.Message, state: FSMContext):
    await delivery(message, state)

@router.message(StateFilter(None), F.text.lower() == '✅')
async def yes_delivery_handler(message: types.Message, state: FSMContext):
    await yes_delivery(message, state)

@router.message(StateFilter(None), F.text.lower() == '❌')
async def no_delivery_handler(message: types.Message, state: FSMContext):
    await no_delivery(message, state)
