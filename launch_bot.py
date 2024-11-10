# Скрипт запуска проекта
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.bot import commands, message_all
from app.bot import set_main_menu
from app.infrastructure.DataBase.DB import Users

import log

from config import Config, load_config

logger = logging.getLogger(__name__)

async def on_startup(bot: Bot):
    logger.info('start bot')
    # await bot.set_my_commands(set_main_menu())

# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    log.get_settings_logger()

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    FakeDataUsers = Users()

    # Инициализируем бот и диспетчер
    logger.info(f'bot token: "{config.tg_bot.token}"')
    bot = Bot(
        config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    logger.info('create bot object')

    # Помещаем нужные объекты в workflow_data диспетчера
    dp.workflow_data.update({'superadmin': config.tg_bot.admin_id,
                             'Users': FakeDataUsers,
                             'users': FakeDataUsers.users})

    # Настраиваем главное меню бота
    await set_main_menu(bot)
    
    # Регистрируем роутеры в диспетчере
    dp.include_router(commands.routet)
    dp.include_router(message_all.routet)

    dp.startup.register(on_startup)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
