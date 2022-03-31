from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.is_admin import IsMe

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')


@dp.message_handler(IsMe())
async def admin_hello(message: types.Message):
    await message.answer('you admin')