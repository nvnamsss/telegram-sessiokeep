import json
import os


class SessionRepository:
    def __init__(self, workdir):
        self.workdir = workdir
        self.sessions = {}
        accounts_path = os.path.join(self.workdir, "accounts.json")
        with open(accounts_path, encoding="utf-8") as f:
            self.accounts = json.load(f)

    def get(self, id: str) -> object:
        session = self.sessions.get(id)
        if session is None or not session["is_available"]:
            return None

        return session

    def get_accounts(self) -> list[object]:
        sessions = [
            file.replace(".session", "")
            for file in os.listdir(self.workdir)
            if file.endswith(".session")
        ]

        for session in sessions:
            with open(
                os.path.join(self.workdir, f"{session}.session"), encoding="utf-8"
            ) as f:
                self.sessions[session] = {}

                if f is not None:
                    self.sessions[session] = json.load(f)
                    self.sessions[session]["is_available"] = True
                    self.sessions[session]["workdir"] = self.workdir
                else:
                    sessions[session] = {"is_available": False}
        return self.sessions

    def get_available_accounts(self) -> list[object]:
        sessions = self.get_accounts()
        results = []

        for session in sessions:
            if session["is_available"]:
                results.append(session)

        return results
