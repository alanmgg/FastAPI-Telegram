from fastapi import FastAPI, Depends, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from . import routers

description = """
Assistant Pepe API supports the introduction of IOT technology in an elevator for people with disabilities 🚀

## Base
We will be able to know if the API is in operation or is stopped through various methods.
"""

openapi_tags = [
    {
        "name": "Base",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Elevator",
        "description": "Routes to manipulate the elevator"
    }
]

app = FastAPI(
    title="Assistant Pepe API",
    description=description,
    version="1.0.0",
    openapi_tags=openapi_tags,
    license_info={
        "name": "MIT License",
        "url": "https://github.com/alanmgg/FastAPI-Telegram/blob/main/LICENSE",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.base.router)
app.include_router(routers.elevator.router)
