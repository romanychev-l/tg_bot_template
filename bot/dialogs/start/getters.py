from typing import TYPE_CHECKING

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from bot.config_data.config import db

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner


async def get_faculties(
    dialog_manager: DialogManager,
    i18n: TranslatorRunner,
    event_from_user: User,
    **kwargs,
) -> dict[str, str]:
    # some getters
    user = db.users.find_one({'tg_id': event_from_user.id})
    faculties = []
    for faculty in db.faculties.find():
        pass

    return {'message_text': i18n.message.selection_faculties(),
            'end_voting': i18n.button.end_voting(),
            'faculties': faculties}