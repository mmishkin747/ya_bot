from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.inline.menu_kb_in import main_kb
from loader import dp


@dp.message_handler(Command(['main']))
async def main_menu(message: types.Message):
    photo_bytes =types.InputFile(path_or_bytesio='static/main.gif')
    await message.answer_photo(photo=photo_bytes, reply_markup=main_kb)


@dp.callback_query_handler(lambda c: c.data=='about')
async def search_handler(call: types.CallbackQuery):
    await call.message.answer(text='В соответствии с законодательством РФ все материалы, а именно, музыкальные файлы, представленные на этом сайте, предназначены исключительно для персонального использования в ознакомительных целях. Все права на них принадлежат их владельцам. После прослушивания загруженного аудиофайла Вы должны приобрести лицензионный компакт-диск (аудиокассету) или удалить этот файл, в противном случае Вы нарушите закон об интеллектуальной собственности.')

