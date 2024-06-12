from pyrogram import Client
from info import API_ID, API_HASH, SESSION

TelegramBot = Client(
  name="TeleBot",
  api_id=API_ID,
  api_hash=API_HASH,
  session_string=SESSION,
  workers = 10
)
