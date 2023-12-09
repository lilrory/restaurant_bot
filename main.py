import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_reader import config
from main_commands import commands
from reservation import reservation_router
from delivery import delivery_router

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(commands.router)
    dp.include_router(reservation_router)
    dp.include_router(delivery_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
