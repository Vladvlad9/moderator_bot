import os
from dotenv import load_dotenv
from os import environ

load_dotenv(".env")
BOT_TOKEN = os.environ["BOT_TOKEN"]
DATABASE = os.environ["DATABASE"]

CHANNEL_URL = os.environ["CHANNEL_URL"]
CHANNEL_ID = os.environ["CHANNEL_ID"]
CHAT_ID = os.environ["CHAT_ID"]

async def load_admins() -> tuple:
    return tuple(map(int, environ["ADMINS"].split(",")))
