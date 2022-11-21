import re
from datetime import datetime

from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram_utils.keyboards import InlineKeyboardButton

import commands
import config
import documents
import texts
import utils
from loader import dp
from utils import is_network_active


class GetMyIp(InlineKeyboardMarkup):
    GET_IP = InlineKeyboardButton(
        text='Дізнатись адресу',
        web_app=WebAppInfo(url=config.GET_IP_URL))

    def __init__(self):
        super().__init__()
        self.add(self.GET_IP)


@dp.message_handler(commands=commands.START)
async def start(msg: types.Message):
    user_id = msg.from_user.id
    user_name = msg.from_user.first_name

    if not documents.User.object(user_id=user_id):
        user = documents.User(user_id=user_id, user_name=user_name)
        user.save()

    await msg.answer(texts.start.format(name=user_name), reply_markup=GetMyIp())


@dp.message_handler(commands=commands.HELP)
async def help_(msg: types.Message):
    await msg.answer(texts.help_)


@dp.message_handler(commands=commands.START)
async def start(msg: types.Message):
    user_id = msg.from_user.id
    user_name = msg.from_user.first_name

    if not documents.User.object(user_id=user_id):
        user = documents.User(user_id=user_id, user_name=user_name)
        user.save()

    await msg.answer(texts.start)


@dp.message_handler(commands=commands.SUBSCRIBE)
async def subscribe(msg: types.Message):
    args = msg.get_args()
    user = documents.User.object(user_id=msg.from_user.id)

    if not args:
        return await msg.answer(texts.subscribe_help)

    if not re.match(utils.IP_REGEX, args):
        return await msg.answer(texts.ip_regex_error)

    user.active_ip = args
    user.notify = True
    user.save()

    await msg.answer(texts.subscribe_success.format(ip=args))

    network_status = is_network_active(user.active_ip)
    report = documents.ElectricityReport(
        user_id=user.user_id,
        ip=user.active_ip,
        status=network_status,
        date=datetime.now(),
    )
    report.save()

    text = texts.electricity_active if network_status else texts.electricity_inactive
    await msg.answer(text)


@dp.message_handler(commands=commands.UNSUBSCRIBE)
async def unsubscribe(msg: types.Message):
    user = documents.User.object(user_id=msg.from_user.id)
    if not user.active_ip:
        return await msg.answer(texts.unsubscribe_error)

    await msg.answer(texts.unsubscribe_success)

    user.active_ip = None
    user.notify = False
    user.save()
