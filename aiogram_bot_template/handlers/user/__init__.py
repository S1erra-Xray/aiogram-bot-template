from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter

from aiogram_bot_template import states
from aiogram_bot_template.filters import ChatTypeFilter, TextFilter
from aiogram_bot_template.keyboards import LangCallback
from . import lang, start


def prepare_user_handler_router() -> Router:
    user_router = Router()
    user_router.message.filter(ChatTypeFilter("private"))

    user_router.message.register(start.start, CommandStart())
    user_router.message.register(
        start.start,
        TextFilter("🏠В главное меню"),  # noqa: RUF001
        StateFilter(states.user.UserMainMenu.menu),
    )

    user_router.message.register(lang.lang, Command("lang"))
    user_router.callback_query.register(LangCallback.filter())

    return user_router
