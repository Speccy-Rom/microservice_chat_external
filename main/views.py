from starlette.responses import JSONResponse
from simple_print import sprint


async def main(request):
    print(request)
    print(dir(request))
    hello = "world"
    sprint(hello, c="green")
    return JSONResponse({"hello": "world"})
