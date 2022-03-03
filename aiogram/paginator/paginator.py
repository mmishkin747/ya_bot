from aiogram import types
from loader import bot, dt_top




def first_page(name_playlist:str , page=1):
    print(dt_top.keys())
    ls_track = dt_top[name_playlist][page]

    media = types.MediaGroup()
    pages = len(dt_top[name_playlist])
    for link in ls_track:
        media.attach_audio(link)
        print(link)
    return (media, page, pages)  


def next_page(name_playlist:str, page_now:int):
    page = page_now+1
    ls_track = dt_top[name_playlist].get(page, None)
    if ls_track:
        media = types.MediaGroup()
        pages = len(dt_top[name_playlist])
        for link in ls_track:
            media.attach_audio(link)
            print(link)
        return (media, page, pages) 
    else:
        return first_page(name_playlist=name_playlist)


def back_page(name_playlist:str, page_now:int):
    page = page_now-1
    ls_track = dt_top[name_playlist].get(page, None)
    pages = len(dt_top[name_playlist])
    if ls_track:
        media = types.MediaGroup()
        for link in ls_track:
            media.attach_audio(link)
        return (media, page, pages) 
    else:
        return first_page(name_playlist=name_playlist, page=pages)



async def del_message(chat_id:int, del_messages:list):
    for id_mes in del_messages:
        await bot.delete_message(chat_id=chat_id, message_id=id_mes)

    






















