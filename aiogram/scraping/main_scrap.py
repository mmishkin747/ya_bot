import requests
from bs4 import BeautifulSoup
import datetime
import json

url = 'https://drivemusic.club/'
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41'}


def main():
    print('----Start_Script----')
    link_pages = add_domain(start_page())
    #print(link_pages)
    link_music = add_domain(get_link(link_pages))
    #print(link_music)
    write_out_link(link_music)
    print("------END--PROGRAM------")


def start_page():
    html_req = requests.get(url, timeout=60, headers=headers)
    soup = BeautifulSoup(html_req.text, "html.parser")
    link_page_out = []
    link_page_ = soup.find_all('a', class_='popular-download-link')
    for link_ in link_page_:
        link_page_out.append(link_.get('href'))
    return(link_page_out)


def add_domain(ls_link:list):
    full_ls_link=[]
    for link in ls_link:
       full_ls_link.append(url[:-1] + link)
    return full_ls_link


def get_link(ls_page:list):
    out_link_ls = []
    for music_get in ls_page:
        link_list_req = requests.get(url=music_get, headers=headers)
        soup_music = BeautifulSoup(link_list_req.text, "html.parser")
        link_ = soup_music.find_all("a", attrs={"class":"song-author-btn btn-download"})[0].get('href')
        out_link_ls.append(link_)
    return out_link_ls


def write_out_link(ls_link:list):
    ls_json = []
    for i in ls_link:
        ls_json.append(
                {'link':i,}
                )
    with open(f'test.json', 'w', encoding="utf-8") as file:
        #fl.write("test")
        #fl.write('\n'.join(ls_link))
        json.dump(ls_json, file, indent=4, ensure_ascii=False)
    print("-----links recorded------")


if __name__ == "__main__":
    main()
