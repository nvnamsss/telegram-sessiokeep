import os
import time
from fastapi import FastAPI, APIRouter
import signal
import sys
import services.session
import controllers.session
import repositories.session
import uvicorn
import logging

from data import config
from rich.logging import RichHandler
import telegram.client

logger = logging.getLogger(__name__)


def run(app):
    uvicorn.run(app, host="0.0.0.0", port=8080)


def list_routes(app: FastAPI):
    routes = []
    for route in app.routes:
        route_info = {
            "path": route.path,
            "name": route.name,
            "methods": route.methods,
        }
        routes.append(route_info)
    return routes


if __name__ == "__main__":
    app = FastAPI()
    logging.basicConfig(
        level=logging.INFO, format="%(message)s", handlers=[RichHandler()]
    )
    telse = APIRouter()

    # adapters
    tel_client = telegram.client.Client(
        api_hash="",
        api_id="",
        workdir="/home/crom/git/airdrops/telegram-sessiokeep/sessions",
    )

    # repositories
    session_repository = repositories.session.SessionRepository(config.WORKDIR)

    # services
    session_service = services.session.SessionService(
        session_repository=session_repository, client=tel_client
    )

    # controllers
    session_controller = controllers.session.SessionController(
        app=telse, session_service=session_service
    )

    app.include_router(telse, prefix="/telse")

    routes = list_routes(app)
    for route in routes:
        logger.info(
            f"Path: {route['path']}, Name: {route['name']}, Methods: {route['methods']}"
        )
    # run
    run(app=app)
