import logging, os
from pyrogram import Client
from info import API_ID, API_HASH, SESSION
from aiohttp import web


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    raise web.HTTPFound(f"https://telegram.me/MeeRazi")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="telebot",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION,
            workers=100,
            plugins={"root": "bot"}
        )

    async def start(self):
        await super().start()
        logging.info(f"Bot started")
        await self.send_message(chat_id="me", text="Bot started")
        #web-server
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", port=os.getenv("PORT", 5051)).start()

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped.")
    
app = Bot()
app.run()