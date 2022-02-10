import aiocron
from channel_box import channel_groups
from simple_print import sprint


@aiocron.crontab("*/1 * * * *", start=False)
async def one_minute_message():
    sprint("one_minute_message", c="red", b="on_white")
    await channel_groups.group_send('group_1', {"username": "CronTab", "message": "Message from aiocron.crontab"})
