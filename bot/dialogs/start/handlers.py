from typing import TYPE_CHECKING
import logging

from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, ManagedMultiselect

from bot.config_data.config import db

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner

logger = logging.getLogger(__name__)


async def checkbox_clicked(callback: CallbackQuery, checkbox: ManagedMultiselect,
                           dialog_manager: DialogManager, item_id: str):
    dialog_manager.dialog_data.update(is_checked=checkbox.is_checked(item_id))


async def button_click(
        callback: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager,
) -> None:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    # some logic
    keyboard = callback.message.reply_markup
    n = len(keyboard.inline_keyboard)
    faculties = []
    
    for i in range(n):
        for j in range(len(keyboard.inline_keyboard[i])):
            if keyboard.inline_keyboard[i][j].text[:1] == '✅':
                faculty = keyboard.inline_keyboard[i][j].text[2:]
                faculties.append(faculty)

    info = db.info.find_one()

    db.users.update_one(
        {'tg_id': callback.message.chat.id},
        {'$set': {'event_' + str(info['active_event']): faculties}}
    )

    await callback.message.answer(text=i18n.message.voting_successfully(), reply_markup=ReplyKeyboardRemove())
    await dialog_manager.done()

    logger.info(f'Voting successfully. Chat id: {callback.message.chat.id}')