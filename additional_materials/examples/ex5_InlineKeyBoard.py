import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

dp = Dispatcher()


@dp.message(Command('start'))
async def start_command(message: types.Message) -> None:
    kb = [
        [types.InlineKeyboardButton(text="Обо мне", callback_data='about_me')],

        [
            types.InlineKeyboardButton(text="Имя", callback_data='name'),
            types.InlineKeyboardButton(text="Портфолио", callback_data='portfolio')
        ],
        [types.InlineKeyboardButton(text="О тебе", callback_data='about_you')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer('Привет! это мой бот-визитка', reply_markup=keyboard)


@dp.callback_query(F.data == "about_me")
async def about_me_callback(callback: types.CallbackQuery):
    await callback.message.answer('Рад, что ты спросил\n'
                                  'Я на самом деле редко говорю о себе, но мама говорит, что я классный')


async def main() -> None:
    token = "token"
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
