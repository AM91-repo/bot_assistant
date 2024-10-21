# Скрипт запуска проекта
import asyncio
import logging

import app.bot
import log

from config import Config, load_config
from environs import Env

LOGGER = logging.getLogger(__name__)
env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение 
                          
BOT_TOKEN = env('BOT_TOKEN')
ADMIN_ID = [env.int('ADMIN_ID')]

if __name__=='__main__':
    # Конфигурируем логирование
    log.get_settings_logger()

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    app.bot.main(config.tg_bot.token, config.tg_bot.admin_id)
