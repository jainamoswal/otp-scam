import os
class vars(object):
    api_id = os.getenv('API_ID', 123456)
    api_hash = os.getenv('API_HASH' ,'abcdefghxxxxx')
    bot_token = os.getenv('BOT_TOKEN', None)
    max = int(os.getenv('MAX', 20))
