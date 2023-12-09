from aiogram import Bot, Router, F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config_reader import config
from main_buttons.buttons import main_kb, delivery_kb, rmk
from utils.states import Form


delivery_router = Router()
bot = Bot(token=config.bot_token.get_secret_value())

@delivery_router.message(StateFilter(None) ,F.text.lower() == '🚘доставка')
async def delivery(message: Message, state: FSMContext):
    await message.answer('👥Укажите ваш номер телефона:', reply_markup=rmk)
    await state.set_state(Form.phone1)

@delivery_router.message(Form.phone1)
async def phone1(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(phone1=message.text)
        await state.set_state(Form.name1)
        await message.answer('👤Укажите ваше имя:')
    else:
        await message.answer(
            '❌Поля заполнены не верно.❌\n\n'
            'Пожалуйста, попробуйте еще раз.',
            reply_markup=main_kb()
        )
        await state.clear()

@delivery_router.message(Form.name1)
async def name_delivery(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        await state.update_data(name1=message.text)
        await state.set_state(Form.address)
        await message.answer('🏠Укажите адрес доставки:')
    else:
        await message.answer(
            '❌Поле заполнены не верно.❌\n\n'
            'Введите свое имя.',
            reply_markup=main_kb()
        )
        await state.clear()

@delivery_router.message(Form.address)
async def address(message: types.Message, state: FSMContext):
        await state.update_data(address=message.text)
        await state.set_state(Form.dishes)
        await message.answer('🍕Укажите блюда, которые хотите заказать:')

@delivery_router.message(Form.dishes)
async def dishes(message: Message, state: FSMContext):
    await state.update_data(dishes=message.text)
    data = await state.get_data()
    await message.answer(
        f'Вы хотите заказать:\n{data["dishes"]}?\n\n'
        f'Ваше имя: {data["name1"]}\n'
        f'Ваш номер телефона: {data["phone1"]}\n'
        f'Адрес доставки: {data["address"]}\n\n',
        reply_markup=delivery_kb()
    )
    await state.set_state()

@delivery_router.message(StateFilter(None), F.text.lower() == '✅')
async def yes_delivery(message: Message, state: FSMContext):
    data = await state.get_data()
    phone1 = data.get('phone1')
    name1 = data.get('name1')
    address = data.get('address')
    dishes = data.get('dishes')
    if phone1 is not None and name1 is not None and address is not None and dishes is not None:
        admin_channel_id = config.admin_channel_id.get_secret_value()
        admin_message = (
            f'‼️Доставка:‼️\n\n'
            f'Телефон: {phone1}\n'
            f'Имя: {name1}\n'
            f'Адрес доставки: {address}\n'
            f'Блюда: {dishes}\n\n'
            f'От пользователя: @{message.from_user.username} (ID: {message.from_user.id})'
        )
        await bot.send_message(admin_channel_id, admin_message)
        await message.answer(
            '✅Ваш заказ успешно оформлен.✅\n\n'
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

@delivery_router.message(StateFilter(None), F.text.lower() == '❌')
async def no_delivery(message: Message, state: FSMContext):
    await message.answer(
        '❌Ваш заказ отменен.❌\n\n'
        'Вы вернулись в главное меню.',
        reply_markup=main_kb()
    )
    await state.clear()
