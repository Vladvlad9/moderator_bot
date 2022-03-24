import string

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
import json


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')

@dp.message_handler(content_types=['sticker'])
async def echo_send(message: types.Message):
    await message.delete()

@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()} \
            .intersection(set(json.load(open('cenz.json')))):
        await message.delete()
