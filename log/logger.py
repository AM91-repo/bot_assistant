import logging.config

from .logging_settings import logging_config

# Загружаем настройки логирования из словаря `logging_config`
def get_settings_logger() -> None:
    logging.config.dictConfig(logging_config)
    