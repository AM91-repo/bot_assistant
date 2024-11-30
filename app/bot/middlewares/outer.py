import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

logger = logging.getLogger(__name__)


class UserIdentificationOuterMiddleware(BaseMiddleware):

    async def __call__(
            self, 
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject, 
            data: Dict[str, Any]
            ) -> Any:
        
        user: User = data.get('event_from_user')
        result = await handler(event, data)

        return result
