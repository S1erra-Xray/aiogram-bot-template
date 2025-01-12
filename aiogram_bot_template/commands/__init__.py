from aiogram import Bot
from aiogram.types import BotCommandScopeChat, BotCommandScopeDefault

from aiogram_bot_template.loader import i18n
from .admins import set_admins_commands
from .default import set_default_commands


async def remove_commands(bot: Bot, id: int = None):
    scope = BotCommandScopeChat(chat_id=id) if id else BotCommandScopeDefault()
    await bot.delete_my_commands(scope=scope)
    for lang in i18n.available_locales:
        await bot.delete_my_commands(scope=scope, language_code=lang)
