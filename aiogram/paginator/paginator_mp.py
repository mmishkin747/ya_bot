from aiogram.types.input_media import MediaGroup



def first_page_mp(user_playlist, page=1):

    dt_user_playlist = cut_list(user_playlist)
    media = make_media_group(ls_tracks=dt_user_playlist[page])
    pages = len(dt_user_playlist)

    return (media, page, pages)  



def next_page_mp(user_playlist:list, page_now:int):
    
    dt_user_playlist = cut_list(ls=user_playlist)
    pages = len(dt_user_playlist)
    if page_now == pages:
        return first_page_mp(user_playlist=user_playlist)
    page = page_now+1
    media = make_media_group(ls_tracks=dt_user_playlist[page])

    return (media, page, pages)


def back_page_mp(user_playlist:list, page_now:int):
    
    dt_user_playlist = cut_list(ls=user_playlist)
    pages = len(dt_user_playlist)
    if page_now == 1:
        page = pages
    else:
        page = page_now-1
    media = make_media_group(ls_tracks=dt_user_playlist[page])

    return (media, page, pages)




def make_media_group(ls_tracks:list):
    media = MediaGroup()
    for audio in ls_tracks:
        media.attach_audio(audio=audio)
    return media


def cut_list(ls:list, count_track:int=10):
    ls_cut = [ls[i:i+count_track] for i in range(0, len(ls), count_track)]
    page=1
    dt_track_pages = dict()
    for ls_page in ls_cut:
        dt_track_pages[page] = ls_page
        page+=1
    return dt_track_pages


