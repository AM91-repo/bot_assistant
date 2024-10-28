# Скрипт запуска проекта
import asyncio
import logging

from aiogram import Bot, Dispatcher
from app.bot import commands, message_all, set_main_menu

import log

from config import Config, load_config

async def on_startup(bot: Bot):
    logger.info('start bot')
    await bot.set_my_commands(set_main_menu())

if __name__=='__main__':
    # Конфигурируем логирование
    log.get_settings_logger()

    logger = logging.getLogger(__name__)

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    logger.info(f'bot token: "{config.tg_bot.token}"')
    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()
    logger.info('create bot object')
    
    dp.include_router(commands.routet)
    dp.include_router(message_all.routet)

    dp.startup.register(on_startup)
    asyncio.run(dp.start_polling(bot))

    # app.bot.main(config.tg_bot.token, config.tg_bot.admin_id)
