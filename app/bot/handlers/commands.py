import logging

from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from random import randint
# from config.config import HELP
from app.bot.lexicon.lexicon_ru import LEXICON_RU, LEXICON_BUDGET_RU
from app.bot.keyboards.keyboard_button import KeyboardBot
from app.bot.keyboards.keyboard_inline import KeyInLine, get_standart_in_line_key
from app.bot.handlers.budget import BudgetCallbackFactory
from app.infrastructure.Users.User import HandlerUser
from app.infrastructure.DataBase.DB import Users

router = Router()
Kd = KeyboardBot()
builder = KeyInLine()

logger = logging.getLogger(__name__)

@router.message(CommandStart())
async def command_start_handler(message: Message, 
                                superadmin: int, 
                                users: list, 
                                Users: Users) -> None:
    '''
    This handler receives messages with `/start` command
    '''
    
    if message.from_user.id not in Users.users:
        Users.users.append(message.from_user.id)
        # logger.info(f'Add new user in list users: {Users.users}')
    logger.info(f'Command "\start" from {message.from_user.username} '+\
                f'id: {message.from_user.id}')
    
    text_admin = ''
    
    if message.from_user.id == superadmin:
        text_admin = 'Вы главный админ, у вас полный доступ'

    Kd.start_menu()

    
    await message.answer(f"Hello, {message.from_user.username}!\n{text_admin}",
                         reply_markup=Kd.get_menu())
    await message.delete()

@router.message(Command(commands='help'))
async def command_help_handler(message: types.Message) -> None:
    logger.info(f'Command "\help" from {message.from_user.username}')
    logger.info(f'Command "\help" from {message.text}')
    Kd.help_menu()

    # await message.reply(text=LEXICON_RU['/help'],
    #                     reply_markup=Kd.get_menu())
    await message.delete()


@router.message(Command(commands='budget'))
async def command_budget_handler(message: types.Message) -> None:
    logger.info(f'in budget mode')
    await message.answer(
        text=LEXICON_BUDGET_RU['start_description'],
        reply_markup=get_standart_in_line_key(
            LEXICON_BUDGET_RU['start_menu'],
            BudgetCallbackFactory,
            user_id=message.from_user.id)
    )
    await message.delete()


@router.message(Command(commands='other'))
async def command_other_handler(message: types.Message) -> None:

    await message.reply(text=LEXICON_RU['other'],
                        reply_markup=Kd.builder_menu()\
                            .as_markup(resize_keyboard=True,
                                       one_time_keyboard=True))
    await message.delete()


@router.message(Command(commands='inline'))
async def command_key_inline(message: types.Message) -> None:
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.in_line_key())


@router.callback_query(F.data == builder.get_name_callback())
async def send_random_value(callback: types.CallbackQuery) -> None:
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer(text='Число сформировано',
                          show_alert=True,
                          reply_markup=callback.message.reply_markup)
