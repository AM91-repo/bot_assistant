from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.button import build_reply_keyboard

router = Router()

@router.message(F.text == "Помощь")
async def help_handler(message: Message):
    """Обработчик команды /help"""
    await message.answer(LEXICON_RU['/help'])

@router.message(F.text == "Задачи")
async def tasks_handler(message: Message):
    """Обработчик команды /tasks"""
    await message.answer("📝 Раздел задач в разработке...")

@router.message(F.text == "Профиль")
async def profile_handler(message: Message):
    """Обработчик команды /profile"""
    await message.answer(
        "👤 Ваш профиль:",
        reply_markup=build_reply_keyboard([['Изменить имя', 'Назад']])
    )

@router.message(F.text == "Назад")
async def back_handler(message: Message):
    """Обработчик кнопки Назад"""
    await message.answer(
        "Главное меню:",
        reply_markup=build_reply_keyboard([LEXICON_RU['reply_buttons']['main']])
    )
    