from pydantic import BaseModel, EmailStr

class Status(BaseModel):
    message: str