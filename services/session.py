import re
import time
from dtos.session import GetTokenRequest
from repositories.session import SessionRepository
from data import config
import pyrogram


class SessionService:
    def __init__(self, session_repository: SessionRepository):
        self.sessions = {}
        self.clients = {}
        self.session_repository = session_repository


    def get_client(self, session_id: str):
        if session_id in self.clients:
            return self.clients[session_id]

        session = self.session_repository.get(session_id)
        if session is None:
            return None

        client = pyrogram.Client(
            name=session_id,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            workdir=session["workdir"],
            lang_code="en",
        )

        self.clients[session_id] = client
        return self.clients.get(session_id)

    def get_chat(self, client: pyrogram.Client, chat_name: str):
        chat = client.get_chat(chat_name)
        messages = client.get_chat_history(chat.id)

        return messages

    def get_otp(self, session_id: str) -> str:
        client = self.get_client(session_id)
        if client is None:
            return {"error": "Session not found"}

        client.start()
        messages = self.get_chat(client, "Telegram")
        last_message = messages[-1]
        pattern = r"Login code:\s(\d{5})"
        match = re.search(pattern, last_message)

        otp = None
        if match:
            otp = match.group(1)
        client.stop()

        return {"otp": otp}

    def get_token(self, req: GetTokenRequest):
        pass        