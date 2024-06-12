import time, asyncio, aiohttp, os, sys
from info import DEPLOY_HOOK, PREFIX
from pyrogram import Client, filters, enums


@Client.on_message(filters.command(["help", "h"], PREFIX) & filters.me)
async def help_cmd(_, message):
    await message.edit_text(
        f"**Commands**\n\n"
        "`.ping` - Check the bot's ping\n"
        "`.urban or .ud <word>` - Get the urban dictionary meaning of the word\n"
        "`.meaning or .m <word>` - Get the meaning of the word\n"
        "`.emoji or .e <emoji>` - To generate emoji text\n"
        "`.facts or .f` - Get random facts\n"
        "`.quotes or .q` - Get random quotes\n"
        "`.ask or .a <question>` - Ask a question\n"
        "`.pfq` - Change your profile picture with random quotes\n"
        "`.bio` - Change your bio with random quotes\n"
        "`.imgq` - Generate image with random quotes\n"
        "`.telegraph` - Create a telegraph post\n"
        "`.song <song name | song url>` - Download song from youtube\n"
        "`.video <video url>` - Download video from youtube\n"
        "`.spam <number> <text>` - Spam the text\n"
        "`.on9 <on | off>` - To activate One9word game cheat\n"
        "`.approve` - Approve all joinRequest\n"
        "`.clearchat` - Delete all chat message from your group\n"
        "`.update` - Deploy the latest changes\n"
        "`.dl` - download from http url\n"
        "`.hack` - Hack animation\n",
        parse_mode=enums.ParseMode.MARKDOWN
    )


@Client.on_message(filters.command("ping", PREFIX) & filters.me)   
async def ping(_, message):
    start = time.time()  
    m = await message.edit("Pong!")
    end = time.time()
    await m.edit(f"Pong! {round(end-start, 2)}s") 

@Client.on_message(filters.command("update", [".", "/"]) & filters.me)
async def deploy(_, message):
    m = await message.edit("Deploying the latest changes...")
    await asyncio.sleep(2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(DEPLOY_HOOK) as resp:
                if resp.status == 200:
                    await m.edit("Deploying...!")
                else:
                    await m.edit("Failed to deploy!")
    except Exception as e:
        await message.edit(f"Error: {str(e)}")    

typing_on = False
@Client.on_message(filters.command("typing", PREFIX) & filters.me)
async def typing(client, message):
    global typing_on
    typing_on = not typing_on
    await message.delete()
    if typing_on:
        while True:
            if not typing_on:
                break
            await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
            await asyncio.sleep(5)
            

playing_on = False
@Client.on_message(filters.command("playing", PREFIX) & filters.me)
async def playing(client, message):
    global playing_on
    playing_on = not playing_on
    await message.delete()
    if playing_on:
        while True:
            if not playing_on:
                break
            await client.send_chat_action(message.chat.id, enums.ChatAction.PLAYING)
            await asyncio.sleep(5)
        
@Client.on_message(filters.command(["spam", "s"], PREFIX) & filters.me)
async def spam_message(_, message):
    _, *text_parts = message.text.split()
    await message.delete()
    try:
        number_of_messages = int(text_parts[0])
        text = ' '.join(text_parts[1:])
    except ValueError:
        number_of_messages = 10
        text = ' '.join(text_parts)
    if text:  # Only send messages if there's text to be spammed
        for _ in range(number_of_messages):
            await message.reply_text(text)

@Client.on_message(filters.command("restart", PREFIX) & filters.me)
async def stop_button(bot, message):
    msg = await message.edit(text="**Process stoped, bot is restarting...**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**Bot restarted**")
    os.execl(sys.executable, sys.executable, *sys.argv)