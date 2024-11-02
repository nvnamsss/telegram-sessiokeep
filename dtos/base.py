from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

class Meta(BaseModel):
    code: int
    message: str
    