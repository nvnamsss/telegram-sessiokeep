import logger
from fastapi import FastAPI, APIRouter


class SessionController:
    def __init__(self, app: FastAPI):
        self.router = APIRouter()
        self.router.add_api_route("/session", self.create, methods=["POST"])
        self.router.add_api_route("/session/{session_id}", self.get, methods=["GET"])

        app.include_router(self.router)

    def create(self, request):
        logger.info("")
        pass

    def get(self, request):
        pass
