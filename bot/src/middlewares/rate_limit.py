from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Any
from database.crud import check_request_limit
from database.session import async_session
from lexicon.lexicon_ru import LEXICON_RU

class RateLimitMiddleware(BaseMiddleware):
    """Ограничение количества запросов"""
    async def __call__(
        self,
        handler: Callable[[Message, dict], Awaitable[Any]],
        event: Message,
        data: dict
    ) -> Any:
        async with async_session() as session:
            if not await check_request_limit(session, event.from_user.id):
                await event.answer(LEXICON_RU['invalid_amount'])
                return
        return await handler(event, data)
    