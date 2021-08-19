from .. import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/proof$', func=lambda e: e.is_private))
async def proof(event):
    await event.reply(file='https://telegra.ph/file/cd07030a6a7a46666cafc.jpg')
    await event.respond(file='https://telegra.ph/file/3ca515c211e645c504d92.jpg')
