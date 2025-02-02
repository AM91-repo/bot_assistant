from aiogram import Router, types
from aiogram.filters import Command
from database.crud import create_user, get_user
from database.session import async_session
from keyboards.inline import main_menu
from aiogram.enums import ParseMode

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    async with async_session() as session:
        user = await get_user(session, message.from_user.id)
        if not user:
            await create_user(
                session,
                message.from_user.id,
                message.from_user.username
            )
            await message.answer("✅ Заявка подана! Ожидайте решения администратора.")
        else:
            await message.answer("⏳ Ваш доступ еще не подтвержден." if not user.is_approved 
                                else "👋 Добро пожаловать!", reply_markup=main_menu())
            