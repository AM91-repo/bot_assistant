import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

LOGGER = logging.getLogger(__name__)


class CallbackFactory(CallbackData, prefix="callback"):
    x: int
    y: int


def get_standart_in_line_key(lst_buttons: list[list], 
                             CallbackFactory: CallbackData,
                             user_id: int) -> InlineKeyboardMarkup:
    array_buttons: list = []

    try:
        for line_buttons in lst_buttons:
            array_buttons.append([])
            # print(line_buttons)
            for button in line_buttons:
                text_button = list(button.keys())[0]
                callbackname = list(button.values())[0]
                array_buttons[-1].append(InlineKeyboardButton(
                    text=text_button,
                    callback_data=CallbackFactory(
                        user_id=user_id, 
                        name_button=callbackname).pack()
                ))
    except Exception as er:
        print(er)
    return InlineKeyboardMarkup(inline_keyboard=array_buttons)


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
    