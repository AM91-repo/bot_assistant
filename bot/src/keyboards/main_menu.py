import logging
from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon_ru import LEXICON_COMMANDS_RU

logger = logging.getLogger(__name__)

async def set_main_menu(bot: Bot) -> None:
    """
    Установка главного меню бота с командами
    :param bot: Объект бота
    """
    try:
        main_menu_commands = [
            BotCommand(
                command=command,
                description=description
            ) for command, description in LEXICON_COMMANDS_RU.items()
        ]
        await bot.set_my_commands(main_menu_commands)
        logger.info("Main menu commands set successfully")
    except Exception as e:
        logger.error(f"Error setting main menu: {e}")
        