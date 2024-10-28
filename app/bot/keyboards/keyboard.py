import logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, BotCommand
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from app.bot.lexicon.lexicon_ru import LEXICON_COMMANDS_RU

LOGGER = logging.getLogger(__name__)


def set_main_menu() -> list[BotCommand]:

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS_RU.items()
    ]

    return main_menu_commands


class KeyInLine():
    def __init__(self) -> None:
        self.builder = InlineKeyboardBuilder()
        # self.dp_callback = dp_callback

    def in_line_key(self):
        self.builder.add(InlineKeyboardButton(
            text="Нажми меня",
            callback_data="random_value"))
        return self.builder.as_markup()
    
    # @staticmethod
    # async def send_random_value(callback: CallbackQuery):
    #     await callback.message.answer(str(random.randint(1, 10)))

    # def apply_callback(self):
    #     decorated_method = self.dp_callback(self.send_random_value)
    #     setattr(self, 'send_random_value', decorated_method)

class KeyboardBot():
    def __init__(self) -> None:
        self.list_keyboard = []
        self._keyboard = None #ReplyKeyboardMarkup(resize_keyboard=True,
                               #             keyboard=self.list_keyboard)
        
    def start_menu(self):
        self.list_keyboard = [
            [KeyboardButton(text="/help")],
            [KeyboardButton(text='/start')],
        ]

    def help_menu(self):
        self.list_keyboard = [
            [KeyboardButton(text="/help"),
            KeyboardButton(text='/start')],
        ]

    def other_menu(self):
        self.list_keyboard = [
            [KeyboardButton(text="Другая команда")],
        ]

    def builder_menu(self):
        LOGGER.debug('menu is bilder')
        builder = ReplyKeyboardBuilder()
        for i in range(1, 32):
            builder.add(KeyboardButton(text=str(i)))
        return builder.adjust(6)

    def get_menu(self):
        LOGGER.debug('menu is set')
        self._keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=self.list_keyboard)
        return self._keyboard
