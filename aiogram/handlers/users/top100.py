from aiogram import types
from loader import dp, db
from paginator.paginator import del_message, first_page, next_page, back_page
from keyboards.inline import pg_button, main_top_kb, main_kb, main_top_years_kb
from aiogram.dispatcher import filters



@dp.callback_query_handler(lambda c: c.data=='top')
async def show_kb_top(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=main_top_kb)


@dp.callback_query_handler(lambda c: c.data=='top_years')
async def top_years(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=main_top_years_kb)



@dp.callback_query_handler(lambda c: c.data=='back_top')
async def back_top100(call: types.CallbackQuery):
     await call.message.edit_reply_markup(reply_markup=main_kb)


@dp.callback_query_handler(lambda c: c.data=='back_years')
async def back_years(call: types.CallbackQuery):
     await call.message.edit_reply_markup(reply_markup=main_top_kb)



# you need write regular expression!!!!! 
@dp.callback_query_handler(filters.Regexp(r'top100\w*'))
async def show_top100(call: types.CallbackQuery):
    await call.answer(text='Подождите! Загружаю плейлист', cache_time=5)
    name_playlist = call.data
    media, page, pages = first_page(name_playlist=name_playlist)
    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text=f'Топ-100 Страница {page} из {pages}',
                                                disable_notification=True,
                                                reply_markup=pg_button)

    user_id = call.message.chat.id
    id_mes_control = send_keyboard.message_id
    id_mes_track_ls = [e['message_id'] for e in send_track_ls]
    id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
    db.add_history(user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track,
                                    name_playlist=name_playlist,
                                    page=page
                                    )
    

@dp.callback_query_handler(lambda c: c.data=='close')
async def close_top100(call: types.CallbackQuery):
    await call.answer(text='Подождите! Удаляю сообщения!')
    user_id = call.message.chat.id
    id_mes_control = call.message.message_id
    id_mes_track = db.get_history(user_id=user_id, id_mes_control=id_mes_control) # получение истории из БД
    if id_mes_track:
        del_messages = id_mes_track[0][2].split()
        del_messages.insert(0, id_mes_control)
        await del_message(chat_id=call.message.chat.id, del_messages=del_messages) # Удаление старых сообщений из чата пагинатором
    try:
        db.del_history(user_id=user_id, id_mes_control=id_mes_control) # удалениие истории из БД
    except Exception as e:
        print(e)



@dp.callback_query_handler(lambda c: c.data=='next_page')
async def next_page_top100(call: types.CallbackQuery):
    await call.answer(text='Подождите! Загружаю плейлист', cache_time=60)   
    history = db.get_history(user_id=call.message.chat.id, id_mes_control=call.message.message_id)
    name_playlist = history[0][3]
    page_now = history[0][4]
    media, page, pages = next_page(name_playlist=name_playlist, page_now=page_now)
    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text=f'Топ-100 Страница {page} из {pages}',
                                                disable_notification=True,
                                                reply_markup=pg_button)
    user_id = call.message.chat.id
    id_mes_control = send_keyboard.message_id
    id_mes_track_ls = [e['message_id'] for e in send_track_ls]
    id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
    db.add_history(user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track,
                                    name_playlist=name_playlist,
                                    page=page
                                    )
    

    

   
@dp.callback_query_handler(lambda c: c.data=='back_page')
async def back_page_top100(call: types.CallbackQuery):
    await call.answer(text='Подождите! Загружаю плейлист', cache_time=60)   
    history = db.get_history(user_id=call.message.chat.id, id_mes_control=call.message.message_id)
    name_playlist = history[0][3]
    page_now = history[0][4]
    media, page, pages = back_page(name_playlist=name_playlist, page_now=page_now)
    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text=f'Топ-100 Страница {page} из {pages}',
                                                disable_notification=True,
                                                reply_markup=pg_button)
    user_id = call.message.chat.id
    id_mes_control = send_keyboard.message_id
    id_mes_track_ls = [e['message_id'] for e in send_track_ls]
    id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
    db.add_history(user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track,
                                    name_playlist=name_playlist,
                                    page=page
                                    )
       

