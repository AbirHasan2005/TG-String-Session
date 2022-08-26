import os

from heroku3 import from_key
from pyrogram import Client
from pyromod import listen

API_ID = int(os.environ.get("API_ID", 18641799))
API_HASH = os.environ.get("API_HASH", 2027706706fd39baf84c01ff5b95a6a6)
BOT_TOKEN = os.environ.get("BOT_TOKEN", 5721954974:AAESDmWWeeM6VHVmu95Fjrzseb4p1sRxtiY)
APP_NAME = os.environ.get("APP_NAME", alonestring)
API_KEY = os.environ.get("API_KEY", None)
HU_APP = from_key(API_KEY).apps()[APP_NAME]

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
