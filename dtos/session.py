from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

from dtos.base import Meta

class GetTokenRequest(BaseModel):
    project_id: str
    session_name: str
    
class GetTokenResponse(BaseModel):
    meta: Meta
    data: str