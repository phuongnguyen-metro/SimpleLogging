from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette_context import context, plugins
from starlette_context.middleware import RawContextMiddleware

from service import SRV
from utils import logger

middleware = [
    Middleware(
        RawContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin()
        )
    )
]

app = FastAPI(middleware=middleware)
svc = SRV()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    logger.info('Endpoint starts')
    svc.hello()
    return {"message": f"Hello {name}"}

