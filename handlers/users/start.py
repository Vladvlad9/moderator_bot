from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.is_admin import IsMe
from keyboards.default.winner import winner_kb

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup = await winner_kb())


@dp.message_handler(chat_type=types.ChatType.SUPERGROUP)
async def log(message: types.Message):
    if message.from_user.first_name != 'Telegram':
        # сюда попадают комменты
        print(message.text) # текст коммента
        print(message.from_user.id) # id user
        print(message.from_user.username) # username
        print(message.reply_to_message.message_id) # id posta

        # await db.update_user(message.from_user.id, message.text, message.from_user.username,
        #                      message.reply_to_message.message_id)

        await db.add_user2(message.reply_to_message.message_id, message.reply_to_message.text, message.from_user.id, message.text, message.from_user.username)
    else:
        # сюда попадают посты
        print(message.message_id) # id posta
        print(message.text) #название поста

        await db.add_user(message.message_id, message.text, message.from_user.id, 'Null', 'Null')


@dp.message_handler(commands=["create_database", "create_db", ])
async def create_database(message: types.Message):
    await message.answer(text="База данных успешно создана!")
    await db.create_all_database()


# @dp.message_handler(IsMe())
# async def admin_hello(message: types.Message):
#     await message.answer('you admin')


