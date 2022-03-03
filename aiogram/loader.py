from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.user_db import Datebase
from utils.google_api import get_tracks
from load_tracks import load_top_playlist



bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Datebase()

# Получение списка треков из гугл драйв через апи ключ
#get_tracks.get_tracks()

# Полученный списовки разрезаются на страницы и хранятся в виде словаря
dt_top = load_top_playlist.load_tracks()


