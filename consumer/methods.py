import json
from channel_box import channel_groups


async def chat_message(message):
    incoming_message_dict = json.loads(message.body.decode())
    await channel_groups.group_send('group_1', {"username": f'{incoming_message_dict["username"]}', "message": f'{incoming_message_dict["message"]}'})
    await message.channel.basic_ack(message.delivery.delivery_tag)
