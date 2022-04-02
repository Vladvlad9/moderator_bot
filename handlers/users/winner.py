from aiogram import types

from keyboards import *
from loader import dp, db

import random


@dp.message_handler(text="Выбрать победителя")
async def back_main_menu(message: types.Message):
    count_users = await db.count_users('Самый первый пост')
    random_user = random.randint(1, int(count_users[0]))
    user_winner = await db.user_winner(random_user, 'Самый первый пост')
    await message.answer(f'Победил пользователь: {user_winner[0][0]} c комментарием {user_winner[0][1]}')