import requests
from bs4 import BeautifulSoup
import json


#url = 'https://myzuka.club/Search?searchText=miyagi'
domain_url = 'https://myzuka.club'
url = 'https://myzuka.club/Hits/Top100Weekly'
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41'}


def main():
    get_link(scrap_page(get_page()))


def get_page():
    page_req = requests.get(url=url, headers=headers)
    print(html_req.status_code)
    #with open('top100.html', 'w') as f:
    #    f.write(html_req.text)
    return page_rep.text


def scrap_page(page_req):
    #with open('top100.html', 'r') as f:
    #    page_req = f.read()
    soup = BeautifulSoup(page_req, "html.parser")
    track_soup =soup.find_all('div', class_='player-inline') 
    out_link = []
    for link in track_soup:
        out_link.append(domain_url + str(link.find('div', class_='top').find('a').get('href')))
    print(f'___получено___ {len(out_link)}') 
    #write_out_link(ls_link=out_link, name_file='ls_page_track.json')
    return out_link


def write_out_link(ls_link:list, name_file: str):
    ls_json = []
    for i in ls_link:
        ls_json.append(
                {'link':i,}
                )
    with open(name_file, 'w', encoding="utf-8") as file:
        json.dump(ls_json, file, indent=4, ensure_ascii=False)
    print("-----links recorded------")


def get_link(link_date):
    ''' На вход получает список ссылок на страницы возвращает список 
        прямых ссылок на песни
    '''
    #with open('ls_page_top100.json', 'r', encoding="utf-8") as file:
    #    link_date = json.load(file)
    #print(link_date[0]['link'])
    link_track_ls = []
    for url in link_date:
        req = requests.get(url['link'], headers=headers)
        print(url['link'])
        print(req.status_code)
        soup = BeautifulSoup(req.text, "html.parser")
        link_track = soup.find('a', class_='button-a dl showdialog no-ajaxy').get('href')
        link_track_ls.append(f'{domain_url}{link_track}')
    write_out_link(ls_link=link_track_ls, name_file='link_top100.json')


if __name__=="__main__":
    main()
