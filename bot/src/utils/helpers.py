from typing import Any
from datetime import datetime

def format_amount(amount: float) -> str:
    """
    Форматирование суммы для вывода
    :param amount: Сумма
    :return: Отформатированная строка
    """
    return f"{amount:.2f} ₽"

def format_history(operations: list[Any]) -> str:
    """
    Форматирование истории операций
    :param operations: Список операций
    :return: Отформатированная строка
    """
    if not operations:
        return "История операций пуста."
    
    formatted_ops = []
    for op in operations:
        op_type = "➕" if isinstance(op, Income) else "➖"
        formatted_ops.append(
            f"{op_type} {op.amount:.2f} ({op.created_at.strftime('%d.%m.%Y %H:%M')})"
        )
    return "\n".join(formatted_ops)

def validate_amount(text: str) -> bool:
    """
    Проверка корректности введенной суммы
    :param text: Введенный текст
    :return: True если сумма корректна
    """
    try:
        amount = float(text.replace(",", "."))
        return amount > 0
    except ValueError:
        return False
    