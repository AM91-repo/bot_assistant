import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from database.models import Base
from database.crud import create_user, get_user
from database.session import engine, async_session

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Database setup
# DATABASE_URL = f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('POSTGRES_DB')}"
# engine = create_async_engine(DATABASE_URL)
# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Импорт обработчиков
from handlers import user, admin, budget
from middlewares import access, rate_limit

# Регистрация middleware
dp.message.middleware(access.AccessMiddleware())
dp.message.middleware(rate_limit.RateLimitMiddleware())

# Регистрация роутеров
dp.include_router(user.router)
dp.include_router(admin.router)
dp.include_router(budget.router)

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    