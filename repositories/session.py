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
        return self.sessions.get(id)

    def get_accounts(self) -> list[object]:
        pass

    def get_available_accounts(self) -> list[object]:
        pass
