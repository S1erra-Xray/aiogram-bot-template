from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter

from aiogram_bot_template.filters import PersonFilter, StatusFilter, TextFilter
from aiogram_bot_template.states import admin
from .start import start
from .users import _users


def prepare_admin_handler_router() -> Router:
    admin_router = Router()
    admin_router.message.filter(PersonFilter("admin"))

    admin_router.message.register(
        _users, Command("users"), StatusFilter(["super_admin"])
    )

    admin_router.message.register(start, CommandStart())
    admin_router.message.register(
        start,
        TextFilter("🏠В главное меню"),  # noqa: RUF001
        StateFilter(admin.AdminMainMenu.menu),
    )

    return admin_router
