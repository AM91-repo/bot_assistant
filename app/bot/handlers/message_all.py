import logging

from aiogram import Router, types
from app.bot.lexicon.lexicon_ru import LEXICON_RU

routet = Router()
logger = logging.getLogger(__name__)

@routet.message()
async def echo_upper(message: types.Message) -> None:
    logger.info(f'from user {message.from_user.username} ' + \
                f'text message: {message.text}')
    await message.answer(text=LEXICON_RU['other_answer'])
