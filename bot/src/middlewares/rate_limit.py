from aiogram import BaseMiddleware
from aiogram.types import Message
from database.crud import check_request_limit
from database.session import async_session
from typing import Callable, Awaitable, Any

class RateLimitMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any]
    ) -> Any:
        async with async_session() as session:
            if not await check_request_limit(session, event.from_user.id):
                await event.answer("⚠️ Превышен лимит запросов! Попробуйте позже.")
                return
        return await handler(event, data)
    