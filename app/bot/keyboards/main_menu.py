import logging
from aiogram.types import BotCommand
from app.bot.lexicon.lexicon_ru import LEXICON_COMMANDS_RU

def set_main_menu() -> list[BotCommand]:

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS_RU.items()
    ]

    return main_menu_commands
