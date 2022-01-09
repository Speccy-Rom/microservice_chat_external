import aiormq
from termcolor import cprint
from consumer import methods
from settings import AMQP_URI
from settings import UNIQUE_PREFIX


async def consumer_subscriptions():
    cprint(f"AMQP CONSUMER:     ready [yes] PREFIX={UNIQUE_PREFIX}", "green")
    connection = await aiormq.connect(AMQP_URI)
    channel = await connection.channel()
    chat_message_queue__declared = await channel.queue_declare(f"{UNIQUE_PREFIX}:external__main:chat_message",
                                                               durable=False)
    await channel.basic_consume(chat_message_queue__declared.queue, methods.chat_message, no_ack=False)
