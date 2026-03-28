import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from bot.config_data.config import config_settings
from bot.dialogs.start.dialogs import start_dialog
from bot.handlers.commands import commands_router
from bot.handlers.other import other_router
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.utils.i18n import create_translator_hub

logging.basicConfig(
    level=config_settings.LOG_LEVEL,
    format="[%(asctime)s] #%(levelname)-8s %(filename)s:"
           "%(lineno)d - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


async def main() -> None:
    bot = Bot(
        token=config_settings.TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher()

    translator_hub: TranslatorHub = create_translator_hub()

    dp.include_router(commands_router)
    dp.include_router(other_router)
    dp.include_router(start_dialog)

    dp.update.middleware(TranslatorRunnerMiddleware())

    setup_dialogs(dp)

    logger.info("Bot starting...")
    try:
        await dp.start_polling(bot, _translator_hub=translator_hub)
    finally:
        await bot.session.close()
        logger.info("Bot stopped")


asyncio.run(main())
