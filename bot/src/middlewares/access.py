from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Any
from database.crud import get_user
from database.session import async_session
from lexicon.lexicon_ru import LEXICON_RU

class AccessMiddleware(BaseMiddleware):
    """Проверка прав доступа пользователя"""
    async def __call__(
        self,
        handler: Callable[[Message, dict], Awaitable[Any]],
        event: Message,
        data: dict
    ) -> Any:
        async with async_session() as session:
            user = await get_user(session, event.from_user.id)
            if not user or not user.is_approved:
                await event.answer(LEXICON_RU['other_answer'])
                return
        return await handler(event, data)
    