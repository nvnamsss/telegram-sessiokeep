import asyncio
import logging
import time
from fastapi import FastAPI, APIRouter

from dtos.base import Meta
from dtos.session import GetQueryIDRequest, GetQueryIDResponse
from services.session import SessionService

logger = logging.getLogger(__name__)


class SessionController:
    def __init__(self, app: APIRouter, session_service: SessionService):
        self.session_service = session_service
        self.router = APIRouter()
        self.router.add_api_route("/ping", self.ping, methods=["GET"])
        self.router.add_api_route("/session", self.create, methods=["POST"])
        self.router.add_api_route("/session/{session_id}", self.get, methods=["GET"])
        self.router.add_api_route("/session/otp", self.get_otp, methods=["GET"])
        self.router.add_api_route(
            "/session/query_id", self.get_query_id, methods=["POST"]
        )
        app.include_router(self.router)

    async def ping(self):
        await asyncio.sleep(5)
        return {"message": "pong"}

    def create(self, request):
        logger.info("")
        pass

    def get(self):
        return {"message": "himom"}

    def get_otp(self, request):
        res = self.session_service.get_otp(request.query_params["session_id"])
        return res

    async def get_query_id(self, request: GetQueryIDRequest):
        logger.info(f"Request: {request}")
        query_id = await self.session_service.get_query_id(request)

        logger.info(f"Query ID: {query_id}")
        return GetQueryIDResponse(
            meta=Meta(status=200, message="success"), data=query_id
        )
