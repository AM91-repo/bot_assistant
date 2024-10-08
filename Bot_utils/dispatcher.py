import asyncio
import logging
import sys
if __name__ == '__main__': sys.path.append('../')

from random import randint
# aiogramm
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from config import TOKEN_API, HELP
from Bot_utils.keyboard import KeyboardBot, KeyInLine

from Users.User import HandlerUser

Kd = KeyboardBot()
dp = Dispatcher()
bot = Bot(TOKEN_API)

async def on_startup():
    print('бот запущен')


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    
    Kd.start_menu()

    await message.answer(f"Hello, {message.from_user.username}!",
                         reply_markup=Kd.get_menu())
    await message.delete()


@dp.message(Command(commands='help'))
async def command_start_handler(message: types.Message) -> None:
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
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))


@dp.message()
async def echo_upper(message: types.Message):
    await message.answer(message.text)


def run_bot() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.startup.register(on_startup)
    asyncio.run(dp.start_polling(bot))


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run_bot()
