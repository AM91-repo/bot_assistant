import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

LOGGER = logging.getLogger(__name__)


class CallbackFactory(CallbackData, prefix="callback"):
    x: int
    y: int


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
    