from aiogram import types
from aiogram.utils.exceptions import TelegramAPIError

import commands
import config
import documents
import texts
from loader import dp


@dp.message_handler(commands=commands.LOGS, user_id=config.ADMIN_ID)
async def logs(msg: types.Message):
    document = types.InputFile(config.LOG_FILE, filename='logs.txt')
    try:
        await msg.answer_document(document)
    except TelegramAPIError:
        await msg.answer(texts.logs_error)


@dp.message_handler(commands=commands.STAT, user_id=config.ADMIN_ID)
async def get_stat(msg: types.Message):
    text = texts.stat.format(
        users=documents.User.objects().count(),
        active_users=documents.User.objects(notify=True).count()
    )
    await msg.answer(text)
