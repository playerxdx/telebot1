from pyrogram import Client, filters
from pyrogram.types import Message
from info import PREFIX
from bot import TelegramBot

emojis = [
    "⁭\n                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n",
    "⁭\n          💛💛💛💛💛💛\n     💛💛💛💛💛💛💛💛\n   💛💛                      💛💛\n 💛💛\n💛💛\n💛💛\n 💛💛\n   💛💛                      💛💛\n     💛💛💛💛💛💛💛💛\n         💛💛💛💛💛💛\n",
    "⁭\n💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                      💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                         💙💙\n💙💙                      💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n",
    "⁭\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟\n💟💟💟💟💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n",
    "⁭\n💚💚💚💚💚💚💚💚\n💚💚💚💚💚💚💚💚\n💚💚\n💚💚\n💚💚💚💚💚💚\n💚💚💚💚💚💚\n💚💚\n💚💚\n💚💚\n💚💚\n",
    "⁭\n          💜💜💜💜💜💜\n     💜💜💜💜💜💜💜💜\n   💜💜                     💜💜\n 💜💜\n💜💜                💜💜💜💜\n💜💜                💜💜💜💜\n 💜💜                        💜💜\n   💜💜                      💜💜\n     💜💜💜💜💜💜💜💜\n          💜💜💜💜💜💜\n",
    "⁭\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n💖💖                        💖💖\n",
    "⁭\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n          💗💗\n💗💗💗💗💗💗\n💗💗💗💗💗💗\n",
    "⁭\n         💛💛💛💛💛💛\n         💛💛💛💛💛💛\n                  💛💛\n                  💛💛\n                  💛💛\n                  💛💛\n💛💛          💛💛\n  💛💛       💛💛\n   💛💛💛💛💛\n      💛💛💛💛\n",
    "⁭\n💙💙                  💙💙\n💙💙             💙💙\n💙💙        💙💙\n💙💙   💙💙\n💙💙💙💙\n💙💙 💙💙\n💙💙     💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                   💙💙\n",
    "⁭\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟\n💟💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟💟\n",
    "⁭\n💚💚                              💚💚\n💚💚💚                      💚💚💚\n💚💚💚💚            💚💚💚💚\n💚💚    💚💚    💚💚    💚💚\n💚💚        💚💚💚        💚💚\n💚💚             💚             💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n",
    "⁭\n💜💜                           💜💜\n💜💜💜                       💜💜\n💜💜💜💜                 💜💜\n💜💜  💜💜               💜💜\n💜💜     💜💜            💜💜\n💜💜         💜💜        💜💜\n💜💜             💜💜    💜💜\n💜💜                 💜💜💜💜\n💜💜                     💜💜💜\n💜💜                          💜💜\n",
    "⁭\n           💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n💗💗\n💗💗\n💗💗\n💗💗\n",
    "⁭\n           💛💛💛💛💛\n      💛💛💛💛💛💛💛\n   💛💛                    💛💛\n 💛💛                        💛💛\n💛💛                           💛💛\n💛💛              💛💛     💛💛\n 💛💛               💛💛 💛💛\n   💛💛                   💛💛\n      💛💛💛💛💛💛💛💛\n           💛💛💛💛💛   💛💛\n",
    "⁭\n💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                     💙💙\n💙💙                     💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n💙💙    💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                  💙💙\n",
    "⁭\n       💟💟💟💟💟\n  💟💟💟💟💟💟💟\n  💟💟                 💟💟\n💟💟\n  💟💟💟💟💟💟\n      💟💟💟💟💟💟\n                            💟💟\n💟💟                 💟💟\n  💟💟💟💟💟💟💟\n       💟💟💟💟💟\n",
    "⁭\n💚💚💚💚💚💚💚💚\n💚💚💚💚💚💚💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n               💚💚\n",
    "⁭\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n  💜💜                  💜💜\n      💜💜💜💜💜💜\n            💜💜💜💜\n",
    "⁭\n💖💖                              💖💖\n  💖💖                          💖💖\n    💖💖                      💖💖\n      💖💖                  💖💖\n         💖💖              💖💖\n           💖💖         💖💖\n             💖💖     💖💖\n               💖💖 💖💖\n                  💖💖💖\n                       💖\n",
    "⁭\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗                               💗💗\n💗💗              💗            💗💗\n 💗💗           💗💗          💗💗\n 💗💗        💗💗💗       💗💗\n  💗💗   💗💗  💗💗   💗💗\n   💗💗💗💗      💗💗💗💗\n    💗💗💗             💗💗💗\n",
    "⁭\n💛💛                    💛💛\n   💛💛              💛💛\n      💛💛        💛💛\n         💛💛  💛💛\n            💛💛💛\n            💛💛💛\n         💛💛 💛💛\n      💛💛       💛💛\n   💛💛             💛💛\n💛💛                   💛💛\n",
    "⁭\n💙💙                    💙💙\n   💙💙              💙💙\n      💙💙        💙💙\n         💙💙  💙💙\n            💙💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n              💙💙\n",
    "⁭\n 💟💟💟💟💟💟💟\n 💟💟💟💟💟💟💟\n                       💟💟\n                   💟💟\n               💟💟\n           💟💟\n       💟💟\n   💟💟\n💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟\n",
    "⁭\n       💗💗💗💗\n   💗💗💗💗💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n💗💗               💗💗\n   💗💗💗💗💗💗\n        💗💗💗💗\n",
    "⁭\n          💙💙\n     💙💙💙\n💙💙 💙💙\n          💙💙\n          💙💙\n          💙💙\n          💙💙\n          💙💙\n     💙💙💙💙\n     💙💙💙💙\n",
    "⁭\n    💟💟💟💟💟\n  💟💟💟💟💟💟\n💟💟          💟💟\n                💟💟\n             💟💟\n          💟💟\n       💟💟\n    💟💟\n  💟💟💟💟💟💟\n  💟💟💟💟💟💟\n",
    "⁭\n     💛💛💛💛\n  💛💛💛💛💛\n💛💛         💛💛\n                   💛💛\n            💛💛💛\n            💛💛💛\n                   💛💛\n💛💛         💛💛\n  💛💛💛💛💛\n     💛💛💛💛\n",
    "⁭\n                         💖💖\n                    💖💖💖\n              💖💖 💖💖\n          💖💖     💖💖\n     💖💖          💖💖\n💖💖               💖💖\n💖💖💖💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖\n                         💖💖\n                         💖💖\n",
    "⁭\n💚💚💚💚💚💚\n💚💚💚💚💚💚\n💚💚\n 💚💚💚💚💚\n   💚💚💚💚💚\n                    💚💚\n                    💚💚\n💚💚          💚💚\n  💚💚💚💚💚\n     💚💚💚💚\n",
    "⁭\n        💜💜💜💜\n    💜💜💜💜💜\n💜💜\n\n💜💜\n💜💜💜💜💜💜\n💜💜💜💜💜💜💜\n💜💜               💜💜\n💜💜               💜💜\n    💜💜💜💜💜💜\n        💜💜💜💜\n",
    "⁭\n💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗\n                      💗💗\n                     💗💗\n                   💗💗\n                 💗💗\n               💗💗\n             💗💗\n           💗💗\n         💗💗\n",
    "⁭\n        💙💙💙💙\n   💙💙💙💙💙💙\n💙💙               💙💙\n💙💙               💙💙\n   💙💙💙💙💙💙\n   💙💙💙💙💙💙\n💙💙               💙💙\n💙💙               💙💙\n   💙💙💙💙💙💙\n        💙💙💙💙\n",
    "⁭\n        💟💟💟💟\n   💟💟💟💟💟💟\n💟💟               💟💟\n💟💟               💟💟\n 💟💟💟💟💟💟💟\n      💟💟💟💟💟💟\n                         💟💟\n                        💟💟\n  💟💟💟💟💟💟\n       💟💟💟💟\n",
]

def convert_to_emoji(text):
    result = ""
    for char in text:
        if char.isalnum():
            index = ord(char.lower()) - ord('a') if char.isalpha() else 26 + int(char)
            result += emojis[index]
        else:
            result += char

    return result


@TelegramBot.on_message(filters.command(["emoji", "e"], PREFIX) & filters.me)
async def emoji(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("Usage: `.emoji <text>`")
        return
    text = message.text.split(maxsplit=1)[1]
    await message.reply(convert_to_emoji(text))