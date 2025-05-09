"""Простой телеграм бот по геншину Версия: 0.0.1"""

import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5536569828:AAGrGNnFKoko_BfZCWaXR5hDrLqkQgEKXbI"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)