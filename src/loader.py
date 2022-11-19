import logging

import mongoengine as me
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram_utils.task_manager import TaskManager

import config

me.connect(
    db=config.MONGO_DB,
    host=config.MONGO_HOST,
    username=config.MONGO_USER,
    password=config.MONGO_PASSWORD,
)

storage = MongoStorage(
    db_name=config.MONGO_DB,
    host=config.MONGO_HOST,
    username=config.MONGO_USER,
    password=config.MONGO_PASSWORD,
)

bot = Bot(
    token=config.BOT_TOKEN,
    parse_mode=types.ParseMode.HTML,
)

dp = Dispatcher(bot, storage=storage)

logging.basicConfig(
    level=20,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('.log', 'w')
    ]
)

log = logging.getLogger()

tm = TaskManager()
