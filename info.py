import os

API_ID = os.getenv("API_ID", "27968778") # Get it from my.telegram.org
API_HASH = os.getenv("API_HASH", "870259949e21603185e5ee820e95ef38") # Get it from my.telegram.org
SESSION = os.getenv("SESSION", "BQGqxQoAFqDdpVziPiKQLNbDXNm1J7sOQH19YLf1olGTRSpldO-qUY8lTe55dukeW-jh9zGVd8oad7_ryXRFDsWB8IBt8flYwo7yVL99OqzZShkNe4xS3CyRDn1NLJhjEMG6rzDzO31_7wxHzQ3DEbD1lhHiY_7b8S188PfXda9uacbr9-AUtddibxzTY_P6vEE2_VBxp8AIWCpXbEvE-0-02kt_N6tqXiCLlM3TNZgLl6AeXNPI0B97P3hxuYylFsOd6aGOOLmeAXg2Vfc5j24AAcrryHMvinF6uBg0yxNhh0KdYA01iHxlzNEZ0saqovz7XMx9YRaXtfUZM0FIF_Qc38xQOwAAAAFzg3VzAA") # Pyrogram Session String (Run session.py to get)
GENAI_API_KEY = os.getenv("GENAI_API_KEY") # Get it from https://makersuit.google.com/
TG_NAME = os.getenv("TG_NAME", "Aakash") # Your Telegram Name (Needed if you wanna use One9word plugins)
DEPLOY_HOOK = os.getenv("DEPLOY_HOOK") # Get it from render.com if you are hosting this bot to RENDER 
PREFIX = os.getenv("PREFIX", ".") # Command Prefix 
ADMIN = int(os.getenv("ADMIN","7100217891")) # Owner User_ID
