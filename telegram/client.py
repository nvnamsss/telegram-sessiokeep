import asyncio
import json
import random
import string
import pyrogram
from aiohttp_socks import ProxyConnector
import pyrogram
from urllib.parse import unquote, quote
from fake_useragent import UserAgent
from urllib.parse import unquote, quote
from aiohttp_socks import ProxyConnector
from faker import Faker


class Client:
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
        self.clients = {}
        for account in self.accounts:
            client = pyrogram.Client(
                name=account["name"],
                api_id=api_id,
                api_hash=api_hash,
                workdir=workdir,
                lang_code="en",
            )
            self.clients[account["name"]] = client

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

    async def get_web_view_url(
        self, session_name, bot_id, bot_shortname, ref_token
    ) -> str:
        client = self.clients[session_name]
        try:
            await client.connect()
            me = await client.get_me()
            if not me.username:
                while True:
                    username = (
                        Faker("en_US").name().replace(" ", "")
                        + "_"
                        + "".join(random.choices(string.digits, k=random.randint(3, 6)))
                    )
                    if await client.set_username(username):
                        logger.success(f"{session_name} | Set username @{username}")
                        break
                asyncio.sleep(5)

            peer_id = await client.resolve_peer(bot_id)
            web_view = await client.invoke(
                pyrogram.raw.functions.messages.RequestAppWebView(
                    peer=peer_id,
                    app=pyrogram.raw.types.InputBotAppShortName(
                        bot_id=peer_id,
                        short_name=bot_shortname,
                    ),
                    platform="android",
                    write_allowed=True,
                    start_param=f"{ref_token}",
                )
            )

            await client.disconnect()
            auth_url = web_view.url
            return auth_url
        except Exception as e:
            logger.error(f"{session_name} | get_tg_web_data | Error: {e}")
            return None
