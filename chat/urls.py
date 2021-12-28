from starlette.routing import Route
from starlette.routing import WebSocketRoute
from .views import Chat
from .views import ChatSocket

routes = [
    Route("/chat", endpoint=Chat, name="chat__chat"),
    WebSocketRoute("/chat_ws", ChatSocket),
]
