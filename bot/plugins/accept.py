from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
import asyncio, logging
from info import PREFIX
from bot import TelegramBot

@TelegramBot.on_message(filters.command(["run", "approve"], PREFIX) & filters.me)                     
async def approve(client: Client, message: Message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True:
           try:
               result = await client.approve_all_chat_join_requests(Id)
               if not result:  # If no join request is pending
                   break         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               result = await client.approve_all_chat_join_requests(Id)
               if not result:  # If no join request is pending
                   break
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))