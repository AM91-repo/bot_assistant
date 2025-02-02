from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from .models import User, Request, Ban

async def create_user(session: AsyncSession, user_id: int, username: str):
    new_user = User(user_id=user_id, username=username)
    session.add(new_user)
    await session.commit()

async def get_user(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).where(User.user_id == user_id))
    return result.scalar()

async def get_pending_users(session: AsyncSession):
    result = await session.execute(select(User).where(User.is_approved == False))
    return result.scalars().all()

async def approve_user(session: AsyncSession, user_id: int):
    user = await get_user(session, user_id)
    if user:
        user.is_approved = True
        await session.commit()

async def ban_user(session: AsyncSession, user_id: int):
    user = await get_user(session, user_id)
    if user:
        new_ban = Ban(user_id=user.id)
        session.add(new_ban)
        await session.commit()

async def check_request_limit(session: AsyncSession, user_id: int):
    last_hour = datetime.utcnow() - timedelta(hours=1)
    result = await session.execute(
        select(func.count()).where(
            Request.user_id == user_id,
            Request.created_at >= last_hour
        )
    )
    return result.scalar() < 15
