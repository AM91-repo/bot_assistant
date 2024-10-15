import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

dp = Dispatcher()


@dp.message(Command('start'))
async def start_command(message: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text="Обо мне")],

        [
            types.KeyboardButton(text="Имя"),
            types.KeyboardButton(text="Портфолио")
        ],
        [
            types.KeyboardButton(text="О тебе")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Привет! это мой бот-визитка', reply_markup=keyboard)


@dp.message(F.text == 'Обо мне')
async def about_me_handler(message: types.Message) -> None:
    await message.answer('Рад, что ты спросил\n'
                         'Я на самом деле редко говорю о себе, но мама говорит, что я классный')


@dp.message(F.text == 'Имя')
async def name_handler(message: types.Message, bot: Bot) -> None:
    await message.answer(f'Меня зовут {(await bot.get_me()).full_name}. '
                         f'А как тебя зовут? Хотя, можешь не отвечать, я не смогу прочитать')


@dp.message(F.text == 'Портфолио')
async def portfolio_handler(message: types.Message) -> None:
    await message.answer('Я пока что только учусь, и ещё не успел создать ботов, но скоро они здесь будут')


@dp.message(F.text == 'О тебе')
async def about_you_handler(message: types.Message) -> None:
    await message.answer(f'А тебя зовут {message.from_user.full_name}!')


async def main() -> None:
    token = "token"
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    