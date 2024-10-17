# Скрипт запуска проекта
import os

import dotenv
import Bot_utils
import logging
import log

from environs import Env

# dotenv.load_dotenv()

LOGGER = logging.getLogger(__name__)
env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение 
                          
BOT_TOKEN = env('BOT_TOKEN')
ADMIN_ID = [env.int('ADMIN_ID')]

# BOT_TOKEN = os.getenv('BOT_TOKEN')
# ADMIN_ID = [os.getenv('ADMIN_ID')]

if __name__=='__main__':
    log.get_settings_logger()
    Bot_utils.main(BOT_TOKEN, ADMIN_ID)
