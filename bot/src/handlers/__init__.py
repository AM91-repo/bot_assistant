# Инициализация обработчиков
from .user import router as user_router
from .admin import router as admin_router
from .budget import router as budget_router
from .common import router as common_router

__all__ = [
    'user_router',
    'admin_router',
    'budget_router',
    'common_router'
]
