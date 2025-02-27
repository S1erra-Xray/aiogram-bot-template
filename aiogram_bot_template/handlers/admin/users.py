from aiogram.types import Message

from aiogram_bot_template.database.models import User
from aiogram_bot_template.loader import _


async def _users(message: Message):
    text, markup = await _get_users_data()
    await message.answer(text, reply_markup=markup)


async def _get_users_data():
    users = await User.get_all()
    if not users:
        return _("Users is empty🫡"), None
    text = ""
    for user in users:
        text += f'\n{"--" * 15}'
        for key, value in user.to_dict().items():
            text += f"\n|{key}: <b>{value}</b>"
    return text, None
