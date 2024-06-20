import os

API_ID = os.getenv("API_ID") # Get it from my.telegram.org
API_HASH = os.getenv("API_HASH") # Get it from my.telegram.org
SESSION = os.getenv("SESSION") # Pyrogram Session String (Run session.py to get this)
GENAI_API_KEY = os.getenv("GENAI_API_KEY") # Get it from https://makersuit.google.com/
TG_NAME = os.getenv("TG_NAME") # Your Telegram Name (Needed if you wanna use One9word plugins)
DEPLOY_HOOK = os.getenv("DEPLOY_HOOK") # Get it from render.com if you are hosting this bot to RENDER 
PREFIX = os.getenv("PREFIX", ".") # Command Prefix 
ADMIN = int(os.getenv("ADMIN")) # Admin ID
DATABASE_URL = os.getenv("DATABASE_URL") # MongoDB Database URL