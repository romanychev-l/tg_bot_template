from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner

from bot.states.actions import Actions

other_router = Router()


@other_router.message(Actions.base_state)
async def handle_base_state(msg: Message, state: FSMContext, i18n: TranslatorRunner):
    await msg.answer(i18n.message.ex_one(), reply_markup=ReplyKeyboardRemove())
