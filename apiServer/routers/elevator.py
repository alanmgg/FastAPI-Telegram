from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from . import db as db_module

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

@router.post("/going-up", tags=["Elevator"])
async def going_up_elevator():
    db_module.crud_elevator.going_up_elevator()
    return db_module.schemas.Status(message="Going up elevator")

@router.post("/going-down", tags=["Elevator"])
async def going_down_elevator():
    db_module.crud_elevator.going_down_elevator()
    return db_module.schemas.Status(message="Going down elevator")