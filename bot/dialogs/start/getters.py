from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from bot.config_data.config import db


async def get_categories(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict:
    categories = []
    async for item in db.categories.find():
        categories.append((item["name"], str(item["_id"])))

    return {
        "message_text": i18n.message.select_categories(),
        "confirm_button": i18n.button.confirm(),
        "categories": categories,
    }
