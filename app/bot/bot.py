'''
Скрипт запуска бота
'''
import sys
if __name__ == '__main__': sys.path.append('../')

from .dispatcher import run_bot


def main(bot_token: str, admin_id: list) -> None:
    run_bot(bot_token, admin_id)


# if __name__ == '__main__':
#     run_bot(bot_token, admin_id)
