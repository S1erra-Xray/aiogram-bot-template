from aiogram import Router

from .chat_type import ChatTypeFilter as ChatTypeFilter
from .person_type import PersonFilter
from .status import StatusFilter, StatusFilter as StatusFilter
from .text import TextFilter as TextFilter


def prepare_filter_router():
    filter_router = Router()
    filter_router.callback_query.filter(ChatTypeFilter("private"))
    filter_router.message.filter(ChatTypeFilter("private"))
    filter_router.inline_query.filter(ChatTypeFilter("private"))

    return filter_router
