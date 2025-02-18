# Инициализация конфигурации
from .config import load_config, Config, DatabaseConfig, TgBot

__all__ = [
    'load_config',
    'Config',
    'DatabaseConfig',
    'TgBot'
]
