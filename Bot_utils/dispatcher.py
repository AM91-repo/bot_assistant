import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from config import TOKEN_API, HELP


dp = Dispatcher()
bot = Bot(TOKEN_API)

kb = [
    [KeyboardButton(text="/help")],
    [KeyboardButton(text='/start')]
]
# key.append(buttom_start)
# key.append(button_help)
# print(key)
keybord = ReplyKeyboardMarkup(resize_keyboard=True,
                              keyboard=kb)
# button_help = KeyboardButton('/help')
# buttom_start = KeyboardButton('/start')
# keybord(buttom_start)
# keybord(button_help)

async def on_startup():
    print('бот запущен')

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hello, {message.from_user.username}!",
                           parse_mode="HTML",
                           reply_markup=keybord)
    await message.delete()

@dp.message(Command(commands='help'))
async def command_start_handler(message: types.Message) -> None:
    await message.reply(text=HELP)
    await message.delete()

@dp.message()
async def echo_upper(message: types.Message):
    await message.answer(message.text)

def run_bot() -> None:
    dp.startup.register(on_startup)
    asyncio.run(dp.start_polling(bot))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run_bot()