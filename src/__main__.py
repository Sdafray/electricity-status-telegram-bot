from aiogram import executor

import commands
from loader import dp


async def on_startup(_):
    import handlers
    import tasks

    handlers.setup()
    tasks.setup()
    await commands.setup()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
