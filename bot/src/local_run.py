import asyncio
from aiogram import Bot, Dispatcher
from database.session import init_db, async_session
from database.models import Base
from handlers import user, admin, budget
from middlewares import access, rate_limit
import os

async def main():
    # Инициализация БД
    await init_db()
    
    # Создаем тестового админа
    async with async_session() as session:
        from database.crud import create_user
        await create_user(session, user_id=int(os.getenv("ADMIN_ID")), username="admin", is_approved=True, is_admin=True)
    
    # Запуск бота
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    
    # Регистрация компонентов
    dp.message.middleware(access.AccessMiddleware())
    dp.message.middleware(rate_limit.RateLimitMiddleware())
    dp.include_router(user.router)
    dp.include_router(admin.router)
    dp.include_router(budget.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    