import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.config import load_config
from database.session import init_db, async_session
from handlers import user, admin, budget, common
from middlewares import access, rate_limit
from keyboards.main_menu import set_main_menu

logging.basicConfig(level=logging.INFO)

async def main():
    """Основная точка входа для запуска бота"""
    config = load_config()
    
    # Инициализация БД
    await init_db()
    
    # Создание администратора
    async with async_session() as session:
        from database.crud import create_user
        await create_user(
            session,
            user_id=config.tg_bot.admin_id,
            username="admin",
            is_approved=True,
            is_admin=True
        )
    
    # Настройка бота
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Регистрация middleware
    dp.message.middleware(access.AccessMiddleware())
    dp.message.middleware(rate_limit.RateLimitMiddleware())
    
    # Регистрация обработчиков
    dp.include_router(user.router)
    dp.include_router(admin.router)
    dp.include_router(budget.router)
    dp.include_router(common.router)
    
    # Настройка главного меню
    await set_main_menu(bot)
    
    # Запуск поллинга
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    