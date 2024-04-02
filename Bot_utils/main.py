'''
Скрипт запуска бота
'''
import sys
if __name__ == '__main__': sys.path.append('../')

from Bot_utils.dispatcher import run_bot


def main() -> None:
    run_bot()


if __name__ == '__main__':
    run_bot()
