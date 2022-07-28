"""
Хендлеры свезанные с клиентами.
Тут будут все команды и обработчки.
"""

from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client


@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Старт', reply_markup=kb_client)
        await message.delete()
    except Exception as ex:
        await message.reply('!!!!')


@dp.message_handler(commands=['Режим_работы'])
async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Режим работы такой.......')


@dp.message_handler(commands=['Расположение'])
async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Адресс')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=['Режим_работы'])
    dp.register_message_handler(place_command, commands=['Расположение'])
