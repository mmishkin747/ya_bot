import requests
from bs4 import BeautifulSoup

#search_text = 'корж'
domain_url = 'https://myzuka.club'

url = 'https://myzuka.club/Search?searchText='
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41'}


def get_search(search_text:str):
    url_search = url+search_text
    req = requests.get(url=url_search, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    #find_table_tracks = soup.find_all('table', class_='table table-condensed table-no-border')
    find_table = soup.find('h1', text='Поиск по композициям').find_next('tr').find_all_next('tr')
    search_ls = list()
    for track in find_table:
        ls = track.find_all('a')
        search_ls.append([ls[0].text, ls[1].text, domain_url+ls[1].get('href')])
    return search_ls


def get_search_track(url):
    req = requests.get(url, headers=headers)
    print(f'{req.status_code} {url}')
    soup = BeautifulSoup(req.text, "html.parser")
    link_track = soup.find('a', class_='button-a dl showdialog no-ajaxy').get('href')
    return f'{domain_url + link_track}'





if __name__=='__main__':
    search_text=input()
    get_search(search_text=search_text)
