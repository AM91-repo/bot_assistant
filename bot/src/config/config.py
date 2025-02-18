from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    """Конфигурация подключения к PostgreSQL"""
    host: str
    port: int
    user: str
    password: str
    database: str

    @property
    def dsn(self) -> str:
        """Строка подключения к БД"""
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

@dataclass
class TgBot:
    """Конфигурация бота"""
    token: str
    admin_id: int
    admin_ids: list[int]

@dataclass
class Config:
    """Общий конфиг приложения"""
    tg_bot: TgBot
    db: DatabaseConfig

def load_config(path: str | None = None) -> Config:
    """Загрузка конфигурации из .env файла"""
    env = Env()
    env.read_env(path)
    
    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"),
            admin_id=int(env("ADMIN_ID")),
            admin_ids=list(map(int, env.list("ADMIN_IDS")))
        ),
        db=DatabaseConfig(
            host=env("DB_HOST", "localhost"),
            port=env.int("DB_PORT", 5432),
            user=env("DB_USER", "postgres"),
            password=env("DB_PASSWORD", "postgres"),
            database=env("DB_NAME", "bot_db")
        )
    )
