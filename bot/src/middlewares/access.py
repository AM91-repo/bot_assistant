from aiogram import BaseMiddleware
from aiogram.types import Message
from database.crud import get_user
from database.session import async_session
from typing import Callable, Awaitable, Any

class AccessMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any]
    ) -> Any:
        async with async_session() as session:
            user = await get_user(session, event.from_user.id)
            if not user or not user.is_approved:
                await event.answer("⏳ Ваш доступ еще не подтвержден!")
                return
        return await handler(event, data)
    