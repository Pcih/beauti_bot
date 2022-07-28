from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Услуги')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Где я', request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).add(b3).insert(b4).add(b5)
# kb_client.row(b1, b2, b3)