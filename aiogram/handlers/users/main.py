from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.inline.menu_kb_in import main_kb
from loader import dp


@dp.message_handler(Command(['main']))
async def main_menu(message: types.Message):
    photo_bytes =types.InputFile(path_or_bytesio='static/main.gif')
    await message.answer_photo(photo=photo_bytes, reply_markup=main_kb)
