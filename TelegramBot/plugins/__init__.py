import os
import importlib

views = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".py") and f != "__init__.py"]

for view in views:
    importlib.import_module(f"TelegramBot.plugins.{view[:-3]}")
    print(f'$ {view} was imported successfully!!')

print(':::::::::::::::::::::: Bot Deployed ::::::::::::::::::::::')
print(':::::::::::: Do join @j_projects at Telegram. ::::::::::::')
