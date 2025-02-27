from aiogram.filters import Filter

from aiogram_bot_template.data import config


class PersonFilter(Filter):
    def __init__(self, type: str):
        self.type = type

    async def __call__(self, update: any, **data) -> bool:
        user = str(update.from_user.id)
        if self.type == "user":
            _is = user not in config.BOT_ADMIN_USER_ID
            return _is
        elif self.type == "admin":
            _is = user in config.BOT_ADMIN_USER_ID
            return _is
