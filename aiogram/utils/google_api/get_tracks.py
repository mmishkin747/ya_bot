import httplib2
import pprint
import sys
from apiclient import discovery
import json
from progress.bar import IncrementalBar
from environs import Env

env = Env()
env.read_env()

link = f'https://drive.google.com/uc?export=download&confirm=no_antivirus&id='

folders_dt = {
    'top100weekly':'19C2QYymAYVbGv4KRu3W9gP2STCXIu8R9',
    'top100mouthly':'1n82QJE0UrJMFrKFy80g3bSL2yAKLWtIh',
    'top100_2022':'1Ojvu7JESGjEVDL2UmWV0kCUhQnOZScAL',
    'top100_2021':'135P2uKD28mZ_OAoZjw624w8tSbahiBF-',
    'top100_2020':'1jorf4PXECO-u05_FXftmLJrzHTPRYrVc',
    'top100_2019':'1XxQKLGTTt86mzg5LhafHiPZlgVq-UDDp',
    'top100_2018':'1bONahmgMP9vV2cWrcdWrhutkzJdyyU6O',
        }

API_KEY = env.str('api_key') # get from API->Credentials page in console.cloud.googl.com
#FOLDER_ID = '1rDGOdxyH1kA8n02nxmhMwCk1A0kTQv9H' # NOTE: folder must be publicly visible when using an API key.
service = discovery.build('drive', 'v3', developerKey=API_KEY)



def printChildren(parent):
    param = {'pageSize': 1000, "q": "'" + parent + "' in parents and mimeType != 'application/vnd.google-apps.folder'"}
    result = service.files().list(**param).execute()
    #print(result)
    files = result.get('files')
    link_files = []
    for afile in files:
        #print(f'File {afile.get("name")}  id_file {afile.get("id")}')
        link_files.append([f'{link+afile.get("id")}', f'{afile.get("name")}'])
    return link_files


def write_out_link(ls_link:list, name_file: str):
    ls_json = []
    bar_2 = IncrementalBar('Получено треков', max=len(ls_link))
    for i in ls_link:
        bar_2.next()
        ls_json.append(
                {'link':i[0],
                'name':i[1]}
                )
    bar_2.finish()
    with open(f"data/link_json/{name_file}.json", 'w', encoding="utf-8") as file:
        json.dump(ls_json, file, indent=4, ensure_ascii=False)



def get_tracks():
    bar_1 = IncrementalBar('Получено списков', max=len(folders_dt))   
    for name_folder, folder_id in folders_dt.items():
        bar_1.next()
        links = printChildren(folder_id)
        write_out_link(ls_link=links, name_file=name_folder)
    bar_1.finish()
    


if __name__=="__main__":
    get_tracks()














