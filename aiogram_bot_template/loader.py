import orjson
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.telegram import TelegramAPIServer
from aiogram.utils.i18n import I18n

from aiogram_bot_template import utils
from aiogram_bot_template.data import config


# Управление языковыми пакетами

i18n = I18n(path=config.I18N_PATH, domain=config.I18N_DOMAIN)
_ = i18n.gettext

# Инстанс бота

aiogram_session_logger = utils.logging.setup_logger().bind(type="aiogram_session")

if config.USE_CUSTOM_API_SERVER:
    session = utils.smart_session.SmartAiogramAiohttpSession(
        api=TelegramAPIServer(
            base=config.CUSTOM_API_SERVER_BASE,
            file=config.CUSTOM_API_SERVER_FILE,
            is_local=config.CUSTOM_API_SERVER_IS_LOCAL,
        ),
        json_loads=orjson.loads,
        logger=aiogram_session_logger,
    )
else:
    session = utils.smart_session.SmartAiogramAiohttpSession(
        json_loads=orjson.loads,
        logger=aiogram_session_logger,
    )
bot = Bot(
    config.BOT_TOKEN,
    session=session,
    default=DefaultBotProperties(parse_mode="HTML"),
)
