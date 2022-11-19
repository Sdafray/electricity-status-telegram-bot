from __future__ import annotations

from datetime import datetime

import mongoengine as me
from aiogram_utils.mongoengine import Document


class User(Document):
    user_id: int = me.IntField()
    user_name: int = me.StringField()
    active_ip: str = me.StringField()
    reg_date: datetime = me.DateTimeField(default=datetime.now())
    notify: bool = me.BooleanField(default=False)


class ElectricityReport(Document):
    user_id: int = me.IntField()
    ip: str = me.StringField()
    date: datetime = me.DateTimeField()
    status: bool = me.BooleanField()
