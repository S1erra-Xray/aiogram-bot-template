from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


_home_btn = InlineKeyboardButton(text="🏠В главное меню", callback_data="admin_home")

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="", callback_data="")]]
)
