from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Помощь", callback_data="help"),
            InlineKeyboardButton(text="Бюджет", callback_data="budget")
        ],
        [
            InlineKeyboardButton(text="Задачи", callback_data="tasks"),
            InlineKeyboardButton(text="Профиль", callback_data="profile")
        ],
        [InlineKeyboardButton(text="Админка", callback_data="admin")]
    ])

def budget_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Мой бюджет", callback_data="my_budget")],
        [
            InlineKeyboardButton(text="➕ Расход", callback_data="expense"),
            InlineKeyboardButton(text="💵 Доход", callback_data="income")
        ],
        [InlineKeyboardButton(text="📅 Планирование", callback_data="planning")]
    ])

def admin_decision_kb(user_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Одобрить", callback_data=f"approve_{user_id}"),
            InlineKeyboardButton(text="⛔ Забанить", callback_data=f"ban_{user_id}")
        ]
    ])
