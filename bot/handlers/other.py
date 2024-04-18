import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import DialogManager, StartMode
from fluentogram import TranslatorRunner

from bot.config_data.config import db
from bot.states.start import StartSG

other_router = Router()


class Actions(StatesGroup):
    base_state = State()


@other_router.message(Actions.base_state)
async def registration_start(msg: Message, state: FSMContext, i18n: TranslatorRunner, dialog_manager: DialogManager):
    # await state.update_data(status='employee')
    
    await msg.answer(i18n.message.ex_one(), reply_markup=ReplyKeyboardRemove())