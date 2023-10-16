import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
API_token = os.getenv("TOKEN")
#print(API_token)

#logging
logging.basicConfig(level=logging.INFO)

#initialise bot and dispatcher

bot=Bot(token=API_token )
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or \help  command
    """

    await message.reply(f"Hi \nI am a Bot\nPrepared by Kakashi!!\n")

@dp.message_handler()
async def echo(message: types.Message):
    """
    This handler receives messages with `/start` or \help  command
    """

    await message.answer(message.text)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)