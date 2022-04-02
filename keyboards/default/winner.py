from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def winner_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        row_width=2,
        resize_keyboard=True,
        one_time_keyboard=False,
        keyboard=[
            [
                KeyboardButton(text="Выбрать победителя")
            ]
        ]
    )
    return keyboard