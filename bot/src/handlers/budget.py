from aiogram import Router, types, F
from database.crud import get_user
from database.session import async_session
from keyboards.inline import budget_menu

router = Router()

@router.message(F.text == "Бюджет")
async def budget_handler(message: types.Message):
    async with async_session() as session:
        user = await get_user(session, message.from_user.id)
        if user and user.is_approved:
            user.mode = "budget"
            await session.commit()
            await message.answer("💰 Режим бюджета:", reply_markup=budget_menu())
            