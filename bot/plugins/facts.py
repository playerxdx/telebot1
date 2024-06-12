from bot.plugins.json import get_json
from pyrogram import Client, filters
from info import PREFIX


@Client.on_message(filters.command(["facts", "f"], PREFIX) & filters.me)
async def get_facts(message):
    data = await get_json(f"https://nekos.life/api/v2/fact")
    fact = data.get('fact')
    if not fact:
        await message.edit(f"Something went wrong!")
    await message.edit(f"{fact}")

