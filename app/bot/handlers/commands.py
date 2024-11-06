import logging

from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from random import randint
# from config.config import HELP
from app.bot.lexicon.lexicon_ru import LEXICON_RU
from app.bot.keyboards.keyboard_button import KeyboardBot
from app.bot.keyboards.keyboard_inline import KeyInLine
from app.infrastructure.Users.User import HandlerUser

routet = Router()
Kd = KeyboardBot()
builder = KeyInLine()

logger = logging.getLogger(__name__)

@routet.message(CommandStart())
async def command_start_handler(message: Message, superadmin) -> None:
    """
    This handler receives messages with `/start` command
    """
    logger.info(f'Command "\start" from {message.from_user.username} '+\
                f'id: {message.from_user.id}')
    
    text_admin = ''
    
    if message.from_user.id == superadmin:
        text_admin = 'Вы главный админ, у вас полный доступ'

    Kd.start_menu()

    
    await message.answer(f"Hello, {message.from_user.username}!\n{text_admin}",
                         reply_markup=Kd.get_menu())
    await message.delete()

@routet.message(Command(commands='help'))
async def command_help_handler(message: types.Message) -> None:
    logger.info(f'Command "\help" from {message.from_user.username}')
    logger.info(f'Command "\help" from {message.text}')
    Kd.help_menu()

    await message.reply(text=LEXICON_RU['/help'],
                        reply_markup=Kd.get_menu())
    await message.delete()


@routet.message(Command(commands='other'))
async def command_other_handler(message: types.Message) -> None:

    await message.reply(text=LEXICON_RU['other'],
                        reply_markup=Kd.builder_menu()\
                            .as_markup(resize_keyboard=True,
                                       one_time_keyboard=True))
    await message.delete()


@routet.message(Command(commands='inline'))
async def command_key_inline(message: types.Message) -> None:
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.in_line_key())


@routet.callback_query(F.data == builder.get_name_callback())
async def send_random_value(callback: types.CallbackQuery) -> None:
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer(text='Число сформировано',
                          show_alert=True,
                          reply_markup=callback.message.reply_markup)
