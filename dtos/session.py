from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

from dtos.base import Meta


class GetQueryIDRequest(BaseModel):
    bot_id: str
    bot_shortname: str
    session_name: str
    ref_token: Optional[str]


class GetQueryIDResponse(BaseModel):
    meta: Meta
    data: str


class GetOTPRequest(BaseModel):
    session_id: str


class GetOTPResponse(BaseModel):
    meta: Meta
    data: str
