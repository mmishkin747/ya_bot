from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu_kb_in import main_kb
from loader import dp, bot
import json
import logging

#@dp.callback_query_handler(lambda callback_query: True)
async def bot_start(callback_query: types.CallbackQuery):

    await callback_query.answer(f"Загружаю плейлист")
    #with open('scraping/link_json/test.json', 'r') as read_file:
     #   date = json.load(read_file)

    #date_0 = date[0]['link']
    #logging.info(f'{date_0}')
    #url = 'https://drivemusic.club/dl/xVBacAcVwz0at-KX1XRnNg/1642646538/download_music/2021/11/nju-nikto.mp3'
    #url2 = 'https://drivemusic.club/dl/6wGvvThsGaaHUtHN2c83jg/1642646540/download_music/2021/11/ahmed-shad-volnaja.mp3'
    #url3 = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1Jucr_6z4P2NfnPucSrJ3T_NVS0SmvH3E'
    #audio_bytes = types.InputFile(path_or_bytesio='static/test_track.mp3')
    #audio_url = types.InputFile(path_or_bytesio=url)
    #await bot.send_audio(callback_query.from_user.id, audio=url)


    await bot.send_audio(callback_query.from_user.id, audio='https://myzuka.club/Song/Download/9349695?t=637782922905991498&s=cbaa24441735b27a701b91dbe9fbf04c')
 
'https://drivemusic.club/dl/ZNsOzEk7EzsBtNsBRfhF-w/1642713091/download_music/2021/11/nju-nikto.mp3'
'https://myzuka.club/Song/Download/9349695?t=637782922905991498&s=cbaa24441735b27a701b91dbe9fbf04c'
