'''
Скрипт запуска бота
'''
if __name__ == '__main__':
    from dispatcher import run_bot
else:
    from Bot_utils.dispatcher import run_bot


def main() -> None:
    run_bot()


if __name__ == '__main__':
    run_bot()
