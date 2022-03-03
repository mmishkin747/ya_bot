import json
import os


#list_test = [i for i in range(1,92)]
dt_top = dict()

   

def open_json(name_file):
    with open(f'data/link_json/{name_file}.json', 'r', encoding='utf-8') as f:
        link_date = json.load(f)
    out_ls = list()
    for link in link_date:
        out_ls.append(link['link'])
    return out_ls


def cut_list(ls:list, count_track:int=10):
    ls_cut = [ls[i:i+count_track] for i in range(0, len(ls), count_track)]
    page=1
    dt_track_pages = dict()
    for ls_page in ls_cut:
        dt_track_pages[page] = ls_page
        page+=1
    return dt_track_pages


def load_tracks():
    file_ls = os.listdir(path='data/link_json/')
    if file_ls:
        for f in file_ls:        
            f = f.split('.')[0]
            dt_top[f] =  cut_list(ls=open_json(name_file=f))
            print(f'Файлы загружены {f}')
    return dt_top
