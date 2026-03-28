import logging

from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, ManagedMultiselect
from fluentogram import TranslatorRunner

from bot.config_data.config import db

logger = logging.getLogger(__name__)


async def checkbox_clicked(
    callback: CallbackQuery,
    checkbox: ManagedMultiselect,
    dialog_manager: DialogManager,
    item_id: str,
):
    dialog_manager.dialog_data.update(is_checked=checkbox.is_checked(item_id))


async def button_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get("i18n")

    keyboard = callback.message.reply_markup
    selected = []

    for row in keyboard.inline_keyboard:
        for btn in row:
            if btn.text.startswith("✅"):
                selected.append(btn.text[2:])

    await db.users.update_one(
        {"tg_id": callback.message.chat.id},
        {"$set": {"selected_categories": selected}},
        upsert=True,
    )

    await callback.message.answer(
        text=i18n.message.selection_saved(),
        reply_markup=ReplyKeyboardRemove(),
    )
    await dialog_manager.done()

    logger.info("Selection saved. Chat id: %s", callback.message.chat.id)
