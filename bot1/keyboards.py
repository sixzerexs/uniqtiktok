from aiogram.types import ReplyKeyboardMarkup, KeyboardButton as kbt

main = ReplyKeyboardMarkup(keyboard=[[kbt(text='Uniqueize')],
                                     [kbt(text='Home')]],
                           resize_keyboard=True,
                           input_field_placeholder='pic action...')