import json
from aiogram import types
from loader import bot

with open('scraping/link_json/link_top100.json', 'r', encoding='utf-8') as f:
    link_date = json.load(f)
    top100_ls = []
    for link in link_date:
        top100_ls.append(link['link'])
    print('open file link top100')


def first_page(list_track=top100_ls, page=1, count_track=10):
    pages = len(list_track) // count_track
    media = types.MediaGroup()

    if pages == 0:
        out_list_track = list_track
        pages = 1
    else:
        out_list_track = list_track[:count_track]

    for link_track in out_list_track:
        media.attach_audio(link_track)

    return (media, page, pages)  


def next_page(page, list_track=top100_ls,  count_track=10):
    pages = len(list_track) // count_track
    media = types.MediaGroup()

    if page+1 == pages:
        out_list_track = list_track[page*count_track:]
    elif page == pages:
        return first_page
    else:
        first_track = (page)*count_track
        end_track = first_track + count_track
        out_list_track = list_track[first_track:end_track]
        print(out_list_track) 

    for link_track in out_list_track:
        media.attach_audio(link_track)
    page += 1 

    return (media, page, pages) 


def back_page(page:int, list_track=top100_ls, count_track=10):
    pages = len(list_track) // count_track
    media = types.MediaGroup()

    if page-1==0:
        print('-------back_page---- 1----------')
        return next_page(page=pages-1)
    elif page==2:
        print('-------back_page---- 2----------')
        return first_page()
    else:
        print('-------back_page---- 3----------')
        first_track = (page)*count_track
        end_track = first_track + count_track
        out_list_track = list_track[first_track:end_track]
        print(out_list_track) 

    for link_track in out_list_track:
        media.attach_audio(link_track)
    page -= 1 
    return (media, page, pages) 



async def del_message(chat_id:int, del_messages:list):
    for id_mes in del_messages:
        await bot.delete_message(chat_id=chat_id, message_id=id_mes)

    






















