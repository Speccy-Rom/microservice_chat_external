import asyncio
from starlette.applications import Starlette
from starlette.routing import Mount
from chat.urls import routes as chat_routes
from main.urls import routes as main_routes
from consumer.subscriptions import consumer_subscriptions
from crontab import one_minute_message
from settings import DEBUG


routes = [
    Mount("/chat", routes=chat_routes),
    Mount("/", routes=main_routes),
]


class AmqpHttpServer(Starlette):
    def __init__(self, *args, **kwargs):
        loop = asyncio.get_event_loop()  # получаем event loop
        loop.create_task(consumer_subscriptions())  # создаем таск
        one_minute_message.start()
        super().__init__(*args, **kwargs)


app = AmqpHttpServer(debug=DEBUG, routes=routes)
