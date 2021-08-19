import logging
from TelegramBot import bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

if __name__ == "__main__":
    from TelegramBot import plugins
    bot.run_until_disconnected()
