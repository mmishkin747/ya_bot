import json

with open('scraping/link_json/test.json', 'r') as read_file:
    date = json.load(read_file)

date_0 = date[0]['link']
print(date_0)

