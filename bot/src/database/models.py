from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    """Модель пользователя"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, index=True)
    username = Column(String(50))
    is_approved = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Связи
    budgets = relationship("Budget", back_populates="user")
    incomes = relationship("Income", back_populates="user")
    expenses = relationship("Expense", back_populates="user")
    bans = relationship("Ban", back_populates="user")
    requests = relationship("Request", back_populates="user")

class Budget(Base):
    """Модель бюджета пользователя"""
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Numeric(10, 2), default=0.00)
    user = relationship("User", back_populates="budgets")

class Income(Base):
    """Модель доходов"""
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user = relationship("User", back_populates="incomes")

class Expense(Base):
    """Модель расходов"""
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user = relationship("User", back_populates="expenses")

class Ban(Base):
    """Модель заблокированных пользователей"""
    __tablename__ = 'bans'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user = relationship("User", back_populates="bans")

class Request(Base):
    """Модель запросов пользователей"""
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String(500))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user = relationship("User", back_populates="requests")
    