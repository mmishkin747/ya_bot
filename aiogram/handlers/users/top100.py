from aiogram import types
#from aiogram.utils.misc import logging
from loader import dp, db
from paginator.paginator_top100 import del_message, first_page, next_page, back_page
from keyboards.inline import page_buttons, main_kb
import logging



test_sql= {}
   

@dp.callback_query_handler(lambda c: c.data=='top100')
async def show_top100(call: types.CallbackQuery):
    media, page, pages = first_page()
    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text=f'Страница {page} из {pages}',
                                                reply_markup=page_buttons)
    user_id = call.message.chat.id
    id_mes_control = send_keyboard.message_id
    id_mes_track_ls = [e['message_id'] for e in send_track_ls]
    id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
    db.add_history( user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track)
    

@dp.callback_query_handler(lambda c: c.data=='close')
async def close_top100(call: types.CallbackQuery):
    photo =types.InputFile(path_or_bytesio='static/main.gif')
    await call.message.answer_photo(photo, reply_markup=main_kb)
    user_id = call.message.chat.id
    id_mes_control = call.message.message_id
    id_mes_track = db.get_history(user_id=user_id, id_mes_control=id_mes_control) # получение истории из БД
    if id_mes_track:
        del_messages = id_mes_track[0][0].split()
        del_messages.append(id_mes_control)
        await del_message(chat_id=call.message.chat.id, del_messages=del_messages) # Удаление старых сообщений из чата пагинатором
    try:
        db.del_history(user_id=user_id, id_mes_control=id_mes_control) # удалениие истории из БД
    except Exception as e:
        print(e)


@dp.callback_query_handler(lambda c: c.data=='next_page')
async def next_page_top100(call: types.CallbackQuery):
    await call.message.answer(text='ok')
    page_now = (call.message.text).split()[1]
    media, page, pages = next_page(page=page_now)
    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text=f'Страница {page} из {pages}',
                                                reply_markup=page_buttons)
    user_id = call.message.chat.id
    id_mes_control = send_keyboard.message_id
    id_mes_track_ls = [e['message_id'] for e in send_track_ls]
    id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
    db.add_history( user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track)
    
    




@dp.callback_query_handler(lambda c: c.data=='back_page')
async def back_page_top100(call: types.CallbackQuery):
    await call.message.answer(text='ok')
    logging.info(call.message.message_id)
    page_now = int(test_sql[call.message.message_id][1])
    logging.info(f'-----------------{page_now}-----------------')
    media, page, pages = back_page(page=page_now)
    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text=f'Страница {page} из {pages}',
                                                reply_markup=page_buttons)
    del test_sql[call.message.message_id]
    test_sql[send_keyboard.message_id]=[send_track_ls, page, pages]
    logging.info(test_sql.keys())
 



"""
# пагинатор 
def top_track (page=1, count=10):
    media = types.MediaGroup()

    if page>=1 and page <=5:
        start_track = (page-1)*count
    else:
        start_track = 0
    end_track = start_track + count
    for track in list_spotify[start_track:end_track]:
        media.attach_audio(f'{link}{track}')
    return media


def next_page(page):
    if page >= 5:
        return 1
    else:
        return page + 1


def back_page(page):
    if page <= 1:
        return 5
    else:
        return page - 1
"""
