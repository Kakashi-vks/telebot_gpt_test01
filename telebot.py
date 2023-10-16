from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types,executor
import openai
import sys

class Reference:
    
    '''
    A class to store previously response from chat gpt
    '''

    def __init__(self)-> None:
        self.response =""

load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")

reference= Reference()

TOKEN=os.getenv("TOKEN")

MODEL_NAME = "gpt-3.5-turbo"

bot= Bot(token=TOKEN)
dp=Dispatcher(bot)

def clear_past():
    ''' function to forget previous comanad'''
    reference.response=""

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` or \help  command
    """

    await message.reply(f"Hi \nI am a Bot\nPrepared by Kakashi!!\nHow can I help you")

@dp.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    This handler receives messages with `\clear  command
    """
    clear_past()
    await message.reply(f"I have cleared past conversation")

@dp.message_handler(commands=['help'])
async def clear(message: types.Message):
    """
    This handler receives messages with ` \help  command
    """
    help_commnad="""
    Hi There I'm chat gpt bot created by Kakashi type folowing
    /start - to start a conversation 
    /clear - to clear the context
    /help - to get help menu 
    """
    await message.reply(help_commnad)

@dp.message_handler()
async def chatgpt(message: types.Message):
    """
    This handler receives user input and gives chat gpt response
    """
    print(f">>>USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = MODEL_NAME,
        messages = [
            {"role": "assistant", "content": reference.response}, 
            {"role": "user", "content": message.text} 
        ]
    )
        
    reference.response=response['choice'][0]['messege']['content']
    print(f">>> ChatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id,text=reference.response)
    

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)