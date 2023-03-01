from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
buttons = [
    InlineKeyboardButton('Backend', callback_data='Backend'),
    InlineKeyboardButton('Frontend', callback_data='Frontend'),
    InlineKeyboardButton('Android', callback_data='Android'),
    InlineKeyboardButton('UIUX', callback_data='UIUX'),
    InlineKeyboardButton('ios', callback_data='ios')
]

button = InlineKeyboardMarkup().add(*buttons)