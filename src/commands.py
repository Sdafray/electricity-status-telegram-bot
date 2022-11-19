from aiogram import types

import config
from loader import dp

REFRESH = 'refresh'
START = 'start'
HELP = 'help'
SUBSCRIBE = 'subscribe'
UNSUBSCRIBE = 'unsubscribe'
LOGS = 'logs'
STAT = 'stat'

USER_COMMANDS = [
    types.BotCommand(HELP, 'Доступні команди'),
    types.BotCommand(SUBSCRIBE, 'Підписатися на повідомлення'),
    types.BotCommand(UNSUBSCRIBE, 'Припинити повідомлення'),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    types.BotCommand(STAT, 'Переглянути статистику'),
    types.BotCommand(LOGS, 'Логи'),
]


async def setup():
    await dp.bot.set_my_commands(USER_COMMANDS)
    await dp.bot.set_my_commands(ADMIN_COMMANDS, scope=types.BotCommandScopeChat(config.ADMIN_ID))
