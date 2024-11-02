import logging
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

LOGGER = logging.getLogger(__name__)

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
    