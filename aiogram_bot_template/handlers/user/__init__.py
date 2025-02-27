from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter

from aiogram_bot_template.filters import PersonFilter, TextFilter
from aiogram_bot_template.keyboards import LangCallback
from aiogram_bot_template.states import user
from . import lang, start


def prepare_user_handler_router() -> Router:
    user_router = Router()
    user_router.message.filter(PersonFilter("user"))

    user_router.message.register(start.start, CommandStart())
    user_router.message.register(
        start.start,
        TextFilter("🏠В главное меню"),  # noqa: RUF001
        StateFilter(user.UserMainMenu.menu),
    )

    user_router.message.register(lang.lang, Command("lang"))
    user_router.callback_query.register(LangCallback.filter())

    return user_router
