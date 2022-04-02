from aiogram import types

from loader import dp


# @dp.message_handler(chat_type=types.ChatType.SUPERGROUP)
# async def log(message: types.Message):
#     if message.from_user.first_name != 'Telegram':
#         # сюда попадают комменты
#         print(message.text) # текст коммента
#         print(message.from_user.id) # id user
#         print(message.from_user.username) # username
#         print(message.reply_to_message.message_id) # id posta
#     else:
#         # сюда попадают посты
#         print(message.message_id) # id posta
#         print(message.text) # text posta
