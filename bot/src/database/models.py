from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    username = Column(String(50))
    is_approved = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    mode = Column(String(20), default='default')
    created_at = Column(DateTime, default=datetime.utcnow)
    bans = relationship("Ban", back_populates="user")
    requests = relationship("Request", back_populates="user")

class Ban(Base):
    __tablename__ = 'bans'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="bans")

class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="requests")
    