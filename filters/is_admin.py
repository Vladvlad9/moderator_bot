from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from data.config import admins


class IsMe(BoundFilter):
    key = 'is_me'

    async def check(self, message: Message) -> bool:
        return message.from_user.id in admins
