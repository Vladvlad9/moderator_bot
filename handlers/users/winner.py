from aiogram import types

from keyboards import *
from loader import dp, db

import random


@dp.message_handler(text="Выбрать победителя")
async def back_main_menu(message: types.Message):

    id_post = await db.get_id_post()
    count_users = await db.count_users(int(id_post[0][0]))

    random_user = random.randint(1, int(count_users[0]))

    user_winner = await db.user_winner(random_user, int(id_post[0][0]))

    await message.answer(f'Победил пользователь: {user_winner[0][0]} c комментарием {user_winner[0][1]}')