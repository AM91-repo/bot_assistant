from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def build_reply_keyboard(buttons: list, resize: bool = True) -> ReplyKeyboardMarkup:
    """
    Строит reply-клавиатуру из списка кнопок
    :param buttons: Список текстов кнопок
    :param resize: Автоматическое изменение размера
    :return: Объект ReplyKeyboardMarkup
    """
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btn) for btn in row] for row in buttons],
        resize_keyboard=resize
    )
