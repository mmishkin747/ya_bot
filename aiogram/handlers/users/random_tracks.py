from keyboards.inline import pg_button_close 
from loader import dp, db, dt_top
from aiogram import types
from random import choices, choice






@dp.callback_query_handler(lambda c: c.data=='random_tracks')
async def search_handler(call: types.CallbackQuery):
    ls = list()
    for values in dt_top.values():
        for value in values.values():
            ls.append(choice(value))
        
    media = types.MediaGroup()
    for track in choices(ls, k=10):
        media.attach_audio(track)

    send_track_ls = await call.message.answer_media_group(media=media)
    send_keyboard = await call.message.answer(text='Случайных 10 треков', reply_markup=pg_button_close)
    user_id = call.message.chat.id
    id_mes_control = send_keyboard.message_id
    id_mes_track_ls = [e['message_id'] for e in send_track_ls]
    id_mes_track = ' '.join(str(e) for e in id_mes_track_ls)
    db.add_history(user_id=user_id, id_mes_control=id_mes_control,
                                    id_mes_track=id_mes_track,
                                    name_playlist='random',
                                    page=1
                                    )
 
