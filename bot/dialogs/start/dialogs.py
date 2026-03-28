import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Button, Group, Multiselect

from bot.dialogs.start.getters import get_categories
from bot.dialogs.start.handlers import checkbox_clicked, button_click
from bot.states.start import StartSG


start_dialog = Dialog(
    Window(
        Format("{message_text}"),
        Group(
            Multiselect(
                checked_text=Format("✅ {item[0]}"),
                unchecked_text=Format("❌ {item[0]}"),
                id="multi_categories",
                item_id_getter=operator.itemgetter(1),
                items="categories",
                on_state_changed=checkbox_clicked,
                min_selected=1,
                max_selected=3,
            ),
            width=2,
        ),
        Button(
            text=Format("{confirm_button}"),
            id="button_confirm",
            on_click=button_click,
        ),
        state=StartSG.start,
        getter=get_categories,
    ),
)
