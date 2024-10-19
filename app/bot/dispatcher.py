import asyncio
import logging
import sys
if __name__ == '__main__': sys.path.append('../')

from random import randint
# aiogramm
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from config.config import HELP
from app.bot.keyboards.keyboard import KeyboardBot, KeyInLine
from app.infrastructure.Users.User import HandlerUser

Kd = KeyboardBot()
dp = Dispatcher()

logger = logging.getLogger(__name__)

async def on_startup():
    pass
    logger.info('start bot')


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    logger.info(f'Command "\start" from {message.from_user.username}')

    Kd.start_menu()

    
    await message.answer(f"Hello, {message.from_user.username}!",
                         reply_markup=Kd.get_menu())
    await message.delete()


@dp.message(Command(commands='help'))
async def command_start_handler(message: types.Message) -> None:
    logger.info(f'Command "\help" from {message.from_user.username}')

    Kd.help_menu()

    await message.reply(text=HELP,
                        reply_markup=Kd.get_menu())
    await message.delete()


@dp.message(Command(commands='other'))
async def command_start_handler(message: types.Message) -> None:

    await message.reply(text=HELP,
                        reply_markup=Kd.builder_menu().as_markup(resize_keyboard=True))
    await message.delete()


@dp.message(Command(commands='inline'))
async def command_key_inline(message: types.Message) -> None:
    builder = KeyInLine()
    # decorator = dp.callback_query(F.data == "random_value")
    # builder.send_random_value = decorator(builder.send_random_value)
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.in_line_key())


@dp.callback_query()
async def send_random_value(callback: types.CallbackQuery) -> None:
    await callback.message.answer(str(randint(1, 10)))


@dp.message()
async def echo_upper(message: types.Message) -> None:
    logger.info('echo answer')
    await message.answer(message.text)


def run_bot(token: str, admin_id: list) -> None:
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info(f'bot token: "{token}"')
    bot = Bot(token)
    logger.info('create bot object')

    dp.startup.register(on_startup)
    asyncio.run(dp.start_polling(bot))


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run_bot()
