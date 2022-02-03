from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db
from .main import main_menu
import sqlite3


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await main_menu(message)
    name = message.from_user.full_name
    user_id = message.from_user.id
    name_playlist = f'Playlist_{user_id}'
    name_history = f'History_{user_id}'
    date = message.date
    print(message)
    try:
        db.add_user(id=message.from_user.id, name=name, 
                language_code=message.from_user.language_code,
                date_add=date)
    except sqlite3.IntegrityError as err:
        print(err)      

    try:
        db.create_table_playlist(name_playlist=name_playlist)
    except Exception as e:
        print(e) 
     
    try:
        db.create_table_history(name_history=name_history)
    except Exception as e:
        print(f'Create_history {e}') 
 

