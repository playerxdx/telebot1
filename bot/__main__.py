from bot import TelegramBot
from bot.server.serve import web_server
import asyncio
from aiohttp import web

async def webrun():
    app = web.AppRunner(await web_server())
    await app.setup()
    site = web.TCPSite(app, "0.0.0.0", 5050)
    await site.start()

async def main():
    web_task = asyncio.create_task(webrun())
    bot_task = asyncio.to_thread(TelegramBot.run)
    await asyncio.gather(web_task, bot_task)

if __name__ == '__main__':
    asyncio.run(main())
