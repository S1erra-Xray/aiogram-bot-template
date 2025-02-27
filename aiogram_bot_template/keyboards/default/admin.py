from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


_home_btn = KeyboardButton(text="🏠В главное меню")

main_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="")]], resize_keyboard=True
)
