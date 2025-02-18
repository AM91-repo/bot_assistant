from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from database.crud import get_pending_users, approve_user, ban_user
from database.session import async_session
from keyboards.inline import admin_decision_kb
from keyboards.button import build_reply_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from config.config import load_config

router = Router()
config = load_config()

@router.message(Command("admin"))
async def admin_panel(message: Message):
    """Панель администратора"""
    if message.from_user.id not in config.tg_bot.admin_ids:
        return await message.answer(LEXICON_RU['other_answer'])
    
    async with async_session() as session:
        pending_users = await get_pending_users(session)
        if not pending_users:
            return await message.answer("✅ Нет новых заявок")
        
        for user in pending_users:
            await message.answer(
                f"👤 Пользователь: @{user.username}",
                reply_markup=admin_decision_kb(user.user_id, LEXICON_RU['admin_actions'])
            )

@router.callback_query(F.data.startswith("approve_"))
async def approve_user_handler(callback: CallbackQuery):
    """Одобрение пользователя"""
    user_id = int(callback.data.split("_")[1])
    async with async_session() as session:
        await approve_user(session, user_id)
        await callback.message.edit_text("✅ Пользователь одобрен!")
        await callback.bot.send_message(
            user_id, 
            "🎉 Ваш доступ подтвержден!", 
            reply_markup=build_reply_keyboard([LEXICON_RU['reply_buttons']['main']])
        )

@router.callback_query(F.data.startswith("ban_"))
async def ban_user_handler(callback: CallbackQuery):
    """Блокировка пользователя"""
    user_id = int(callback.data.split("_")[1])
    async with async_session() as session:
        await ban_user(session, user_id)
        await callback.message.edit_text("⛔ Пользователь заблокирован!")
