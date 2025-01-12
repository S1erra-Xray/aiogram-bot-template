from aiogram import Router
from aiogram.filters import Command

from aiogram_bot_template.filters import ChatTypeFilter, StatusFilter
from users import _users


def prepare_admin_handler_router() -> Router:
    admin_router = Router()
    admin_router.message.filter(ChatTypeFilter("private"))

    admin_router.message.register(
        _users, Command("users"), StatusFilter(["super_admin"])
    )
    return admin_router
