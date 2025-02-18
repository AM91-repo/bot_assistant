from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from database.crud import get_user, create_user
from database.session import async_session
from keyboards.inline import build_inline_keyboard
from keyboards.button import build_reply_keyboard
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    """Обработчик команды /start"""
    async with async_session() as session:
        user = await get_user(session, message.from_user.id)
        if not user:
            await create_user(
                session,
                message.from_user.id,
                message.from_user.username or ""
            )
            await message.answer(
                LEXICON_RU['/start'],
                reply_markup=build_reply_keyboard([LEXICON_RU['reply_buttons']['main']])
            )
        else:
            status_msg = (LEXICON_RU['other_answer'] 
                        if not user.is_approved 
                        else "👋 Добро пожаловать!")
            await message.answer(
                status_msg,
                reply_markup=build_reply_keyboard([LEXICON_RU['reply_buttons']['main']])
            )
            