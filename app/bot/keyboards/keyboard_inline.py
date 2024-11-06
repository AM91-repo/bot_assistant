import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

LOGGER = logging.getLogger(__name__)

class KeyInLine():
    def __init__(self) -> None:
        self.kb_builder = InlineKeyboardBuilder()
        self.callback_name = "random_value"
        # self.dp_callback = dp_callback

    def get_name_callback(self):
        return self.callback_name

    def in_line_key(self) -> InlineKeyboardMarkup:
        self.kb_builder.add(InlineKeyboardButton(
            text="Нажми меня",
            callback_data=self.callback_name))
        return self.kb_builder.as_markup()
    