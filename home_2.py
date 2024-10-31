import random, asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import token

bot = Bot(token=token)
dp = Dispatcher()

lucky_number = random.choice([1, 2, 3])

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer("Отгодайте число от 1 до 3")

@dp.message()
async def random(message:Message):
    number = int(message.text)    
    if number == lucky_number:
        await message.answer_photo("https://yandex.ru/images/search?p=1&text=Скидварт+с+надписью+Win&pos=27&rpt=simage&img_url=https%3A%2F%2Ffunny.klev.club%2Fuploads%2Fposts%2F2024-03%2Ffunny-klev-club-p-smeshnie-kartinki-so-skvidvardom-2.jpg&from=tabbar&lr=10310", caption='ТЫ выиграл!')
    elif number != lucky_number:
        await message.answer_photo("https://yandex.ru/images/search?p=1&text=МИСТЕР+КРАБ&pos=8&rpt=simage&img_url=https%3A%2F%2Fimages.gamebanana.com%2Fimg%2Fembeddables%2FMod_402600_sd_image.jpg%3F1663605309&from=tabbar&lr=10310",caption="ТЫ проиграл лох")
    else:
        await message.answer("Ошибка")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")