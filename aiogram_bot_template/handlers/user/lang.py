from aiogram.types import CallbackQuery, Message

from aiogram_bot_template.database.models import get_session, User
from aiogram_bot_template.keyboards import get_lang_markup, LangCallback
from aiogram_bot_template.loader import _


async def lang(message: Message):
    await message.answer(_("Select language:"), reply_markup=get_lang_markup())


async def lang_callback(call: CallbackQuery, callback_data: LangCallback):
    async with get_session() as session:
        await User.update(session, call.from_user.id, lang=callback_data.lang)
    await call.message.edit_text(
        _("Language changed!", locale=callback_data.lang), reply_markup=None
    )
