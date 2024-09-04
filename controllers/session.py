import logger
from fastapi import FastAPI, APIRouter

from services.session import SessionService


class SessionController:
    def __init__(self, app: FastAPI, session_service: SessionService):
        self.session_service = session_service
        self.router = APIRouter()
        self.router.add_api_route("/session", self.create, methods=["POST"])
        self.router.add_api_route("/session/{session_id}", self.get, methods=["GET"])
        self.router.add_api_route("/session/otp", self.get_otp, methods=["GET"])
        app.include_router(self.router)

    def create(self, request):
        logger.info("")
        pass

    def get(self, request):
        pass

    def get_otp(self, request):
        res = self.session_service.get_otp(request.query_params["session_id"])
        return res
