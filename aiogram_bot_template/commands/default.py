from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

from aiogram_bot_template.loader import _, i18n


def get_default_commands(lang: str = "en"):
    commands = [
        BotCommand(command="/start", description=_("start chat", locale=lang)),
        BotCommand(command="/lang", description=_("change language", locale=lang)),
    ]

    return commands


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.set_my_commands(
            get_default_commands(lang),
            scope=BotCommandScopeDefault(),
            language_code=lang,
        )
