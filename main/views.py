from starlette.responses import JSONResponse
from starlette.requests import Request
from simple_print import sprint


async def main(request: Request) -> JSONResponse:
    welcome_message = "rabbitmq learn welcome message"
    sprint(welcome_message, c="green")
    return JSONResponse({"rabbitmq learn": "welcome message"})
