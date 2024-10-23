import logging

from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from random import randint
from config.config import HELP
from app.bot.keyboards.keyboard import KeyboardBot, KeyInLine
from app.infrastructure.Users.User import HandlerUser

routet = Router()
Kd = KeyboardBot()

logger = logging.getLogger(__name__)

@routet.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    logger.info(f'Command "\start" from {message.from_user.username}')

    Kd.start_menu()

    
    await message.answer(f"Hello, {message.from_user.username}!",
                         reply_markup=Kd.get_menu())
    await message.delete()

@routet.message(Command(commands='help'))
async def command_start_handler(message: types.Message) -> None:
    logger.info(f'Command "\help" from {message.from_user.username}')

    Kd.help_menu()

    await message.reply(text=HELP,
                        reply_markup=Kd.get_menu())
    await message.delete()


@routet.message(Command(commands='other'))
async def command_start_handler(message: types.Message) -> None:

    await message.reply(text=HELP,
                        reply_markup=Kd.builder_menu().as_markup(resize_keyboard=True))
    await message.delete()


@routet.message(Command(commands='inline'))
async def command_key_inline(message: types.Message) -> None:
    builder = KeyInLine()
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.in_line_key())


@routet.callback_query()
async def send_random_value(callback: types.CallbackQuery) -> None:
    await callback.message.answer(str(randint(1, 10)))
