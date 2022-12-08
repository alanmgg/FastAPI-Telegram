from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from . import db as db_module
import env

router = APIRouter()

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.post("/going-up", tags=["Elevator"], response_model=db_module.schemas.Status)
async def going_up_elevator():
    db_module.crud_elevator.going_up_elevator()
    return db_module.schemas.Status(message="Going up elevator")

@router.post("/going-down", tags=["Elevator"], response_model=db_module.schemas.Status)
async def going_down_elevator():
    db_module.crud_elevator.going_down_elevator()
    return db_module.schemas.Status(message="Going down elevator")

@router.post("/send-file", tags=["Elevator"], response_model=db_module.schemas.Status)
async def send_file():
    response = db_module.crud_elevator.send_file()
    if response == True:
        return db_module.schemas.Status(message="File sent to Telegram")
    else:
        return db_module.schemas.Status(message="Error sending file, more information on Telegram")

@router.post("/invalid-command", tags=["Elevator"], response_model=db_module.schemas.Status)
async def invalid_command():
    db_module.crud_elevator.invalid_command()
    return db_module.schemas.Status(message="Invalid command")