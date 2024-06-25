from aiogram.types import ReplyKeyboardMarkup, KeyboardButton as kbt

main = ReplyKeyboardMarkup(keyboard=[[kbt(text='Uniq photo')]],
                           resize_keyboard=True,
                           input_field_placeholder='pic action...')