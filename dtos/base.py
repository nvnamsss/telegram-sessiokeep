from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

class Meta(BaseModel):
    status: int
    message: str
    