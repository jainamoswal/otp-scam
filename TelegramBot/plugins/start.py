from .. import bot
from telethon import events, Button

link = 'https://t.me/share/url?url=Hello!!&text=Check%20this%20bot%20which%20can%20send%20SMS%20anonymously%20from%20telegram.%20Bot:%20@sMs_scambot'

@bot.on(events.NewMessage(pattern='/start$', func=lambda e: e.is_private))
async def user_joined(event):
    await event.reply(file='CAADAgADAQEAAladvQoivp8OuMLmNAI')
    await event.respond('I\'m a simple bot that can send SMS to anyone in India.\n\nDo join @j_projects and share this Bot. ♥️♥️', buttons=Button.url('Share this bot.', link), link_preview=False)
                
