# Инициализация основного модуля
from .main import main
from .local_run import main as local_run

__all__ = [
    'main',
    'local_run'
]
