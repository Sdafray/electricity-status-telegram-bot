from datetime import datetime

import config
import documents
import texts
from loader import tm, dp
from utils import is_network_active


@tm.forever(sleep_time=config.CHECK_INTERVAL)
async def check_status_and_send_message():
    for user in documents.User.objects():

        if not user.notify:
            continue
        if not user.active_ip:
            continue

        network_status = is_network_active(user.active_ip)

        reports = [*documents.ElectricityReport.objects(user_id=user.user_id, ip=user.active_ip)]
        reports.sort(key=lambda x: x.date)
        previously_report = reports[-1]

        report = documents.ElectricityReport(
            user_id=user.user_id,
            ip=user.active_ip,
            status=network_status,
            date=datetime.now(),
        )

        if network_status:
            if not previously_report.status:
                report.save()
                out_time = datetime.now() - previously_report.date
                text = texts.electricity_active_time.format(time=':'.join(str(out_time).split(':')[:2]))
                await dp.bot.send_message(text=text, chat_id=user.user_id)
        else:
            if previously_report.status:
                report.save()
                await dp.bot.send_message(text=texts.electricity_inactive, chat_id=user.user_id)
