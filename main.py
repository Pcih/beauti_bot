from aiogram.utils import executor
from create_bot import dp
from hendlers import client, admin, other


async def on_startup(_):
    print('all ok')

client.register_handlers_client(dp)
other.other_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
