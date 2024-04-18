import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.kbd import Button, Group, Multiselect

from bot.dialogs.start.getters import get_faculties
from bot.dialogs.start.handlers import checkbox_clicked, button_click
from bot.states.start import StartSG


start_dialog = Dialog(
    Window(
        # some window
        Format('{message_text}'),
        Group(
            Multiselect(
                checked_text=Format('✅ {item[0]}'),
                unchecked_text=Format('❌ {item[0]}'),
                id='multi_faculties',
                item_id_getter=operator.itemgetter(1),
                items="faculties",
                on_state_changed=checkbox_clicked,
                min_selected=1,
                max_selected=3,
            ),
            width=2
        ),
        Button(
            text=Format('{end_voting}'),
            id='button_voting_end',
            on_click=button_click,
            # when='button_status'
        ),
        state=StartSG.start,
        getter=get_faculties,
    ),
)