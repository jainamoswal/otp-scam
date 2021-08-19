from .. import bot
from telethon import events

help_text='''
I'm the one bot who can send SMS to indian numbers using CollageSearch API creds which got exposed.

**▵ Commands ▵**
/start - __To start the bot.__
/proof - __To get proof.__
/send - __To send a OTP. (SMS)__
/help - __To see this message again. __

**≜ Conditions ≜**
1. Message must not be longer than 20 words. `(maybe)`
2. Recepient must be Indian number.
3. SMS will arrive from CollageSearch as "<your message> is your CollegeSearch Mobile Verification OTP."
4. No guarantee of SMS as CollageSearch may chnage the Creds periodically.
'''

@bot.on(events.NewMessage(pattern='/help$', func=lambda e: e.is_private))
async def user_joined(event):
    await event.reply(help_text)
                
