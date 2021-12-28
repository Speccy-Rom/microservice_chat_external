from starlette.applications import Starlette
from starlette.routing import Mount
from chat.urls import routes as chat_routes
from main.urls import routes as main_routes
from settings import DEBUG
from crontab import one_minute_message


routes = [
    Mount("/chat", routes=chat_routes),
    Mount("/", routes=main_routes),
]


class AmqpHttpServer(Starlette):
    def __init__(self, *args, **kwargs):
        one_minute_message.start()
        super().__init__(*args, **kwargs)


app = AmqpHttpServer(debug=DEBUG, routes=routes)
