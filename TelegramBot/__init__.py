from telethon import TelegramClient
from config import vars

bot = TelegramClient('bot_session', vars.api_id, vars.api_hash).start(bot_token=vars.bot_token) 
