import asyncio
from aiogram import Bot, Dispatcher, types

dp = Dispatcher()


@dp.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer('Подождите, пожалуйста, я думаю...')
    await asyncio.sleep(3)
    await message.send_copy(chat_id=message.chat.id)


async def main() -> None:
    token = "token"
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    