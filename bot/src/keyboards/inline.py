from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon_ru import LEXICON_RU

def build_inline_keyboard(buttons_config: list) -> InlineKeyboardMarkup:
    """
    Строит инлайн-клавиатуру из конфигурации
    :param buttons_config: Конфигурация кнопок из словаря LEXICON_RU
    :return: Объект InlineKeyboardMarkup
    """
    keyboard = []
    for row in buttons_config:
        keyboard_row = []
        for button in row:
            keyboard_row.append(
                InlineKeyboardButton(
                    text=button['text'],
                    callback_data=button['callback']
                )
            )
        keyboard.append(keyboard_row)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def admin_decision_kb(user_id: int, lexicon: dict) -> InlineKeyboardMarkup:
    """
    Клавиатура для админских действий
    :param user_id: ID пользователя
    :param lexicon: Словарь с текстами кнопок
    :return: Объект InlineKeyboardMarkup
    """
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text=lexicon['approve'],
            callback_data=f"approve_{user_id}"
        ),
        InlineKeyboardButton(
            text=lexicon['ban'],
            callback_data=f"ban_{user_id}"
        )
    ]])

# Добавляем функцию main_menu
def main_menu() -> InlineKeyboardMarkup:
    """
    Главное меню с командами
    :return: Объект InlineKeyboardMarkup
    """
    return build_inline_keyboard(LEXICON_RU['main_menu']['buttons'])
