import aiohttp
from pyrogram import Client, filters
from info import PREFIX

async def get_quotes():
    url = "https://api.quotable.io/quotes/random"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                quote_data = await response.json()
                
                # Check if the response is a list of quotes
                if isinstance(quote_data, list) and len(quote_data) > 0:
                    quote = quote_data[0]
                    return quote.get("content", None)
                
                # If not a list, assume it's a single quote
                return quote_data.get("content", None)
            else:
                return None

@Client.on_message(filters.command(["quotes", "q", "quote"], PREFIX) & filters.me)
async def get_quote(_, message):
    quotes = await get_quotes()
    await message.edit(f"{quotes}")

@Client.on_message(filters.command("bio", PREFIX) & filters.me)
async def change_bio(client, message):
    try:
        msg = await message.edit("Changing bio...")
        while True:
            quote = await get_quotes()
            if len(quote) <= 70:
                await client.update_profile(bio=quote)
                await msg.edit(f"**Bio has been changed to:** {quote}")
                break    
    except Exception as e:
        await message.edit(f"An error occurred: {e}")       