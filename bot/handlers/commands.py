from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.states.start import StartSG

commands_router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
    msg: Message,
    dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)
