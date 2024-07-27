import os

API_ID = os.getenv("API_ID", "27968778") # Get it from my.telegram.org
API_HASH = os.getenv("API_HASH", "870259949e21603185e5ee820e95ef38") # Get it from my.telegram.org
SESSION = os.getenv("SESSION", BQGqxQoAMWBe8TqBq-iqvz-uPJfkC26kgN4HduMkaOfXieWdApWduV8YZUQw1BuEA5RACQxnCfIR9RvLyCn-BgvPYaur_6crUUBXWcusNPk_RsPrZUS0550WdBZ1-MhMfnBgZadBz6rKvLtNgXRjbe7JZ8sgfBIfeoJqFr9IPFvNOBvzRXGQzx6kxHHfAz-ukzyfGFFaNmr4tYzMNMBJnQGRef0Axz6upBRd-N8KbedcGjYlSKROtfa3xiPNABiJOn3ngL_Zee-TzrbCnotCGuaHkWA0zlIiI2Eeiw4NAwkRhOxC_tMan6WWI-34GjWmvmKaJPOQ1C42V8Xw1QcRuqqZroFXlgAAAAGQszlEAA"") # Pyrogram Session String (Run session.py to get)
GENAI_API_KEY = os.getenv("GENAI_API_KEY") # Get it from https://makersuit.google.com/
TG_NAME = os.getenv("TG_NAME", "Aakash") # Your Telegram Name (Needed if you wanna use One9word plugins)
DEPLOY_HOOK = os.getenv("DEPLOY_HOOK") # Get it from render.com if you are hosting this bot to RENDER 
PREFIX = os.getenv("PREFIX", ".") # Command Prefix 
ADMIN = int(os.getenv("ADMIN","7100217891")) # Owner User_ID
