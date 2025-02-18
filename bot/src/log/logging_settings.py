import sys

from .log_filters import DebugWarningLogFilter, CriticalLogFilter, ErrorLogFilter


logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_1': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_2': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_3': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(message)s'
        }
    },
    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter,
        },
        'error_filter': {
            '()': ErrorLogFilter,
        },
        'debug_warning_filter': {
            '()': DebugWarningLogFilter,
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'stderr': {
            'class': 'logging.StreamHandler',
        },
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_2',
            # 'formatter': 'default',
            'filters': ['debug_warning_filter'],
            'stream': sys.stdout,
        },
        'debag_file': {
            'class': 'logging.FileHandler',
            'filename': 'log/logs/debag.log',
            'mode': 'w',
            'level': 'DEBUG',
            'formatter': 'formatter_2',
            'filters': ['debug_warning_filter'],
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': 'log/logs/error.log',
            'mode': 'w',
            'level': 'DEBUG',
            'formatter': 'formatter_1',
            'filters': ['error_filter'],
        },
        'critical_file': {
            'class': 'logging.FileHandler',
            'filename': 'log/logs/critical.log',
            'mode': 'w',
            'formatter': 'formatter_3',
            'filters': ['critical_filter'],
        }
    },
    'loggers': {
        '__main__': {
            'level': 'DEBUG',
            'handlers': ['stdout', 'debag_file'],

        },
        'app.bot.handlers.commands': {
            'level': 'DEBUG',
            'handlers': ['stdout', 'debag_file'],

        },
        'app.bot.handlers.message_all': {
            'level': 'DEBUG',
            'handlers': ['stdout'],
        },
        'app.bot.keyboard': {
            'level': 'DEBUG',
            'handlers': ['stdout', 'critical_file'],
        },
        'aiogram.dispatcher': {
            'level': 'INFO',
            'handlers': ['stdout'],
        },
    },
    # 'root': {
    #     'formatter': 'default',
    #     'handlers': ['default'],
    # },
}
