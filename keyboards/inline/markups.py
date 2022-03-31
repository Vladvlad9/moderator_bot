from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



async def channel_ikb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1
    )
    keyboard.add(*[InlineKeyboardButton(text="Канал", callback_data=f"channel")])
    return keyboard