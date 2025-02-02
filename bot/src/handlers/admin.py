from aiogram import Router, types, F
from database.crud import get_pending_users, approve_user, ban_user
from database.session import async_session
from keyboards.inline import admin_decision_kb
import os

router = Router()

@router.message(F.text == "Админка")
async def admin_panel(message: types.Message):
    if message.from_user.id != int(os.getenv("ADMIN_ID")):
        return await message.answer("🚫 Доступ запрещен!")
    
    async with async_session() as session:
        pending_users = await get_pending_users(session)
        if not pending_users:
            return await message.answer("✅ Нет новых заявок")
        
        for user in pending_users:
            await message.answer(
                f"👤 Пользователь: @{user.username}",
                reply_markup=admin_decision_kb(user.user_id)
            )

@router.callback_query(F.data.startswith("approve_"))
async def approve_user_handler(callback: types.CallbackQuery):
    user_id = int(callback.data.split("_")[1])
    async with async_session() as session:
        await approve_user(session, user_id)
        await callback.message.answer(f"✅ Пользователь одобрен!")
        await callback.bot.send_message(user_id, "🎉 Ваш доступ подтвержден!", reply_markup=main_menu())

@router.callback_query(F.data.startswith("ban_"))
async def ban_user_handler(callback: types.CallbackQuery):
    user_id = int(callback.data.split("_")[1])
    async with async_session() as session:
        await ban_user(session, user_id)
        await callback.message.answer(f"⛔ Пользователь забанен!")
        