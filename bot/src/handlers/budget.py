from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.crud import (
    get_budget, 
    update_budget,
    add_income,
    add_expense,
    get_history
)
from database.session import async_session
from keyboards.inline import build_inline_keyboard
from keyboards.button import build_reply_keyboard
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

class BudgetStates(StatesGroup):
    waiting_amount = State()
    waiting_new_budget = State()

@router.message(F.text == "Бюджет")
async def budget_main(message: Message):
    """Главное меню бюджета"""
    await message.answer(
        LEXICON_RU['budget_menu']['start_description'],
        reply_markup=build_inline_keyboard(LEXICON_RU['budget_menu']['buttons'])
    )

@router.callback_query(F.data == "my_budget")
async def show_budget(callback: CallbackQuery):
    """Показать текущий бюджет"""
    async with async_session() as session:
        budget = await get_budget(session, callback.from_user.id)
        amount = budget.amount if budget else 0.0
        await callback.message.edit_text(
            LEXICON_RU['budget_menu']['current_budget'].format(amount=amount),
            reply_markup=build_inline_keyboard(LEXICON_RU['budget_menu']['buttons'])
        )

@router.callback_query(F.data == "edit_budget")
async def edit_budget(callback: CallbackQuery, state: FSMContext):
    """Редактирование бюджета"""
    await callback.message.answer(
        LEXICON_RU['budget_menu']['adjust_budget'],
        reply_markup=build_reply_keyboard([['Отмена']])
    )
    await state.set_state(BudgetStates.waiting_new_budget)

@router.message(BudgetStates.waiting_new_budget, F.text.regexp(r"^\d+([.,]\d{1,2})?$"))
async def process_new_budget(message: Message, state: FSMContext):
    """Обработка новой суммы бюджета"""
    amount = float(message.text.replace(",", "."))
    async with async_session() as session:
        await update_budget(session, message.from_user.id, amount)
        await message.answer(
            LEXICON_RU['operation_success'],
            reply_markup=build_inline_keyboard(LEXICON_RU['budget_menu']['buttons'])
        )
    await state.clear()

@router.callback_query(F.data == "history")
async def show_history(callback: CallbackQuery):
    """Показать историю операций"""
    async with async_session() as session:
        incomes, expenses = await get_history(session, callback.from_user.id)
        operations = []
        for inc in incomes:
            operations.append(f"➕ {inc.amount:.2f} ({inc.created_at.strftime('%d.%m.%Y')})")
        for exp in expenses:
            operations.append(f"➖ {exp.amount:.2f} ({exp.created_at.strftime('%d.%m.%Y')})")
        
        await callback.message.answer(
            LEXICON_RU['budget_menu']['history_header'].format(
                operations="\n".join(operations[-10:])
            ),
            reply_markup=build_inline_keyboard(LEXICON_RU['budget_menu']['buttons'])
        )
        