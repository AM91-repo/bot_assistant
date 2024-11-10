import logging

from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters.callback_data import CallbackData

router = Router()

class BudgetCallbackFactory(CallbackData, prefix='budget'):
    user_id: int
    name_button: str


@router.callback_query(BudgetCallbackFactory.filter())
async def process_budget(callback: CallbackQuery,
                         callback_data: BudgetCallbackFactory):
    
    await callback.message.answer(
        text=f'{callback_data.user_id}, {callback_data.name_button}'
    )

    await callback.answer()