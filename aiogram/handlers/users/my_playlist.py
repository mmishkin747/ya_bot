from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from google.auth import impersonated_credentials
from loader import dp, db
import sqlite3
from keyboards.inline import pg_button_mp, create_pl_button
from paginator.paginator_mp import first_page_mp, next_page_mp, back_page_mp
from states import Create_playlist_state, Search_state




@dp.message_handler(content_types='audio')
async def get_audio(message: types.Message):
    name_playlist = f'Playlist_{message.from_user.id}'
    try:
        db.add_track(name_playlist=name_playlist, id_track=message.audio.file_id,
                    uniq_id=message.audio.file_unique_id, name_track=message.audio.file_name)

        await message.answer(f'Песня добавленна в Ваш плейлист!')
    except sqlite3.IntegrityError as err:
        print(err)
        await message.answer('Трек был сохраненн ранее.')
    finally:
        await message.delete()


@dp.message_handler(content_types='audio',state=Search_state.search_state_2)
async def get_audio_search(message: types.Message):
    await get_audio(message=message)
 


@dp.callback_query_handler(lambda c: c.data=='my_playlist')
async def show_my_playlist(call: types.CallbackQuery):
    user_id = call.message.chat.id
    playlist_db = db.select_myplaylist(user_id=user_id)
    print(playlist_db)
    if len(playlist_db) >= 2:
        user_playlist=list()
        for i in playlist_db:
            user_playlist.append(i[0])
        print(user_playlist)
        await call.answer(text=f'{len(user_playlist)} у вас треков в плейлисте')
        media, page, pages = first_page_mp(user_playlist=user_playlist)
        send_track_ls = await call.message.answer_media_group(media=media)
        send_keyboard = await call.message.answer(text=f'Мой плейлист. Страница {page} из {pages}',
                                                disable_notification=True,
                                                reply_markup=pg_button_mp)

        user_id = call.message.chat.id
        id_mes_control = send_keyboard.message_id
        id_mes_track_ls = [e['message_id'] for e in send_track_ls]
        id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
        db.add_history(user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track,
                                    name_playlist='my_playlist',
                                    page=page
                                    )
  
    elif len(playlist_db) == 1:
        await call.message.answer_audio(audio=playlist_db[0][0])

    else:
        await call.message.answer(text=f'У Вас нету треков в плейлисте \n'
                            'Пришли мне трек и я добвлю его в твой плейлист')


@dp.callback_query_handler(lambda c: c.data=='next_page_mp')
async def next_page_top100(call: types.CallbackQuery):
    user_id = call.message.chat.id
    history = db.get_history(user_id=call.message.chat.id, id_mes_control=call.message.message_id)
    page_now = history[0][4]
 
    playlist_db = db.select_myplaylist(user_id=user_id)

    user_playlist=list()
    for i in playlist_db:
        user_playlist.append(i[0])
    print(user_playlist)
    await call.answer(text=f'{len(user_playlist)} у вас треков в плейлисте')
    media, page, pages = next_page_mp(user_playlist=user_playlist, page_now=page_now)
    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text=f'Мой плейлист. Страница {page} из {pages}',
                                                disable_notification=True,
                                                reply_markup=pg_button_mp)

    user_id = call.message.chat.id
    id_mes_control = send_keyboard.message_id
    id_mes_track_ls = [e['message_id'] for e in send_track_ls]
    id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
    db.add_history(user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track,
                                    name_playlist='my_playlist',
                                    page=page
                                    )
  


@dp.callback_query_handler(lambda c: c.data=='back_page_mp')
async def next_page_top100(call: types.CallbackQuery):
    user_id = call.message.chat.id
    history = db.get_history(user_id=call.message.chat.id, id_mes_control=call.message.message_id)
    page_now = history[0][4]
 
    playlist_db = db.select_myplaylist(user_id=user_id)

    user_playlist=list()
    for i in playlist_db:
        user_playlist.append(i[0])
    print(user_playlist)
    await call.answer(text=f'{len(user_playlist)} у вас треков в плейлисте')
    media, page, pages = back_page_mp(user_playlist=user_playlist, page_now=page_now)
    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text=f'Мой плейлист. Страница {page} из {pages}',
                                                disable_notification=True,
                                                reply_markup=pg_button_mp)

    user_id = call.message.chat.id
    id_mes_control = send_keyboard.message_id
    id_mes_track_ls = [e['message_id'] for e in send_track_ls]
    id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
    db.add_history(user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track,
                                    name_playlist='my_playlist',
                                    page=page
                                    )

# описать модель поведения в редактирование плейлиста, добавить состояние редакторование плейлиста

@dp.callback_query_handler(text='create_playlist')
async def create_playlist(call: types.CallbackQuery):
    await call.message.edit_text( text='Пришли мне трек который хочешь удалить!',reply_markup=create_pl_button)
    await Create_playlist_state.create_state.set()


@dp.callback_query_handler(lambda c: c.data=='delete_all', state=Create_playlist_state.create_state)
async def delete_all(call: types.CallbackQuery, state: FSMContext):
    playlist_name = f'Playlist_{call.from_user.id}'
    db.delete_all_tracks(name_playlist=playlist_name)
    await state.reset_state()
    await call.message.answer(text=f'Все треки удалены с Вашего плейлиста /main')


@dp.message_handler(content_types='audio', state=Create_playlist_state.create_state )
async def del_audio(message: types.Message):
    name_playlist = f'Playlist_{message.from_user.id}'
    uniq_id = message.audio.file_unique_id
    name_track = message.audio.file_name
    print(uniq_id)
    print(name_playlist)
    db.delete_track(name_playlist=name_playlist, uniq_id=uniq_id)
    await message.answer(text=f'Трек {name_track} удален')

@dp.callback_query_handler(lambda c:c.data=='close_create_pl', state=Create_playlist_state.create_state)
async def close_edit(call: types.CallbackQuery, state= FSMContext):
    await call.message.answer(text=f'Редактирование закрыто. /main')
    await state.reset_state()
 
















