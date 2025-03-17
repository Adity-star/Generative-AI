import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# For logging
logging.basicConfig(level=logging.INFO)

#Initalize bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    await message.reply ("Hi\n I Am Hawk Bot!\n Powered by AK")


@dp.message_handler()
async def echo(message: types.Message):
    """ It will return echoo"""
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)