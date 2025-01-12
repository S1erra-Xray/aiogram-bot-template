from aiogram import Router

from .chat_type import ChatTypeFilter as ChatTypeFilter
from .status import StatusFilter, StatusFilter as StatusFilter
from .text import TextFilter as TextFilter


def prepare_filter_router():
    admin_status = ["admin", "super_admin"]
    filter_router = Router()
    filter_router.callback_query.filter(StatusFilter(admin_status))
    filter_router.message.filter(StatusFilter(admin_status))
    filter_router.inline_query.filter(StatusFilter(admin_status))

    return filter_router
