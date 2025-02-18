from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .models import Base  
from config.config import load_config


DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Создание движка с использованием конфига
# engine = create_async_engine(config.db.dsn)
# async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

engine = create_async_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
