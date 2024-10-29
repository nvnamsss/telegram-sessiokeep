import json

import pyrogram


class Client():
    def __init__(self, api_id, api_hash, workdir):
        self.api_id = api_id
        self.api_hash = api_hash
        self.workdir = workdir

        # join path
        account_path = f"{workdir}/accounts.json"
        # load from json file
        with open(account_path) as f:
            self.accounts = json.load(f)
            
        print(f"Accounts: {self.accounts}")
        self.clients = []
        for account in self.accounts:
            client = pyrogram.Client(
                name=account["name"],
                api_id=api_id,
                api_hash=api_hash,
                workdir=workdir,
                lang_code='en',
            )
            self.clients.append(client)
        # self.client = pyrogram.Client(
        #     name=session_name,
        #     phone_number=phone_number,
        #     api_id=api_id,
        #     api_hash=api_hash,
        #     proxy=proxy,
        #     workdir=workdir,
        # )
        #
        # read config
        # create clients from config
    def start(self):
        pass

    def stop(self):
        pass

    def get_chat(self, chat_name):
        pass

    def get_chat_history(self, chat_id):
        pass
    
    async def get_web_view_url(self) -> str:
        
        pass