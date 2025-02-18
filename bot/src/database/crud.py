from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from .models import User, Request, Ban, Budget, Income, Expense
import logging

logger = logging.getLogger(__name__)

async def get_user(session: AsyncSession, user_id: int) -> User | None:
    """
    Получение пользователя по ID
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя в Telegram
    :return: Объект пользователя или None
    """
    result = await session.execute(select(User).where(User.user_id == user_id))
    return result.scalars().first()

async def get_budget(session: AsyncSession, user_id: int) -> Budget | None:
    """
    Получение текущего бюджета пользователя
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя
    :return: Объект бюджета или None
    """
    result = await session.execute(select(Budget).where(Budget.user_id == user_id))
    return result.scalar()

async def create_user(
    session: AsyncSession, 
    user_id: int, 
    username: str, 
    is_approved: bool = False, 
    is_admin: bool = False
) -> User:
    """
    Создание нового пользователя
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя в Telegram
    :param username: Имя пользователя
    :param is_approved: Статус подтверждения
    :param is_admin: Является ли администратором
    :return: Созданный пользователь
    """
    existing_user = await get_user(session, user_id)
    if existing_user:
        logger.info(f"User {user_id} already exists")
        return existing_user
    
    new_user = User(
        user_id=user_id,
        username=username,
        is_approved=is_approved,
        is_admin=is_admin
    )
    session.add(new_user)
    await session.commit()
    return new_user

async def get_pending_users(session: AsyncSession) -> list[User]:
    """
    Получение списка неподтвержденных пользователей
    :param session: Асинхронная сессия БД
    :return: Список пользователей
    """
    result = await session.execute(select(User).where(User.is_approved == False))
    return result.scalars().all()

async def approve_user(session: AsyncSession, user_id: int) -> None:
    """
    Подтверждение пользователя
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя
    """
    user = await get_user(session, user_id)
    if user:
        user.is_approved = True
        await session.commit()

async def ban_user(session: AsyncSession, user_id: int) -> None:
    """
    Блокировка пользователя
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя
    """
    user = await get_user(session, user_id)
    if user:
        new_ban = Ban(user_id=user.id)
        session.add(new_ban)
        await session.commit()

async def check_request_limit(session: AsyncSession, user_id: int) -> bool:
    """
    Проверка лимита запросов (15/час)
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя
    :return: True если лимит не превышен
    """
    last_hour = datetime.utcnow() - timedelta(hours=1)
    result = await session.execute(
        select(func.count()).where(
            Request.user_id == user_id,
            Request.created_at >= last_hour
        )
    )
    return result.scalar() < 15

async def update_budget(session: AsyncSession, user_id: int, amount: float) -> None:
    """
    Обновление бюджета пользователя
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя
    :param amount: Сумма для изменения
    """
    budget = await session.execute(select(Budget).where(Budget.user_id == user_id))
    budget = budget.scalar()
    if budget:
        budget.amount += amount
    else:
        new_budget = Budget(user_id=user_id, amount=amount)
        session.add(new_budget)
    await session.commit()

async def add_income(session: AsyncSession, user_id: int, amount: float) -> None:
    """
    Добавление дохода
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя
    :param amount: Сумма дохода
    """
    new_income = Income(user_id=user_id, amount=amount)
    session.add(new_income)
    await update_budget(session, user_id, amount)

async def add_expense(session: AsyncSession, user_id: int, amount: float) -> None:
    """
    Добавление расхода
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя
    :param amount: Сумма расхода
    """
    new_expense = Expense(user_id=user_id, amount=amount)
    session.add(new_expense)
    await update_budget(session, user_id, -amount)

async def get_history(session: AsyncSession, user_id: int) -> tuple[list[Income], list[Expense]]:
    """
    Получение истории операций
    :param session: Асинхронная сессия БД
    :param user_id: ID пользователя
    :return: Кортеж (доходы, расходы)
    """
    incomes = await session.execute(
        select(Income)
        .where(Income.user_id == user_id)
        .order_by(Income.created_at.desc())
        .limit(10)
    )
    expenses = await session.execute(
        select(Expense)
        .where(Expense.user_id == user_id)
        .order_by(Expense.created_at.desc())
        .limit(10)
    )
    return incomes.scalars().all(), expenses.scalars().all()
