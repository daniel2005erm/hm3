from aiogram import Bot,Dispatcher,types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from keys import button
import os
import logging
load_dotenv(".env")

bot = Bot(os.environ.get('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здраствуйте {message.from_user.first_name}")
    await message.reply("Какое напровление вы предпочитаете: /Backend , /Frontend , /Android , /UIUX , /ios", reply_markup=button)

@dp.callback_query_handler(lambda call: call)
async def all(call):
    if call.data == "Backend":
        await backend(call.message)
    elif call.data == "Frontend":
        await frontend(call.message)
    elif call.data == "Android":
        await android(call.message)
    elif call.data == "UIUX":
        await ui(call.message)
    elif call.data == "ios":
        await ios(call.message)

@dp.message_handler(commands='Backend')
async def backend(message:types.Message):
    await message.reply("Backend — это внутренняя часть сайта и сервера и т.д \nСтоимость 10000 сом в месяц \nОбучение: 5 месяц")

@dp.message_handler(commands='Frontend')
async def frontend(message:types.Message):
    await message.reply("Frontend - это внешний вид сайта \nСтоимость 10000 сом в месяц \nОбучение: 7 месяц")

@dp.message_handler(commands='Android')
async def android(message:types.Message):
    await message.reply("Android - это создание приложений \nСтоимоть 10000сом в месяц \nОбучение: 7 месяц")

@dp.message_handler(commands='UIUX')
async def ui(message:types.Message):
    await message.reply("UI-UX - это создание дизайн сайта его внешний вид и т.д \nСтоимость 10000 в месяц \nОбучение: 3 месяц")

@dp.message_handler(commands='ios')
async def ios(message:types.Message):
    await message.reply("ios - это создание приложение только для продукции iPhone \nСтоимость 10000 в месяц \nОбучение: 6 месяц")

@dp.message_handler()
async def not_found(message: types.Message):
    await message.reply("я вас не понимаю, вот мои команды: /Backend , /Frontend , /Android , /UIUX , /ios")

executor.start_polling(dp)