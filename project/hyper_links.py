from queue import Empty
from bs4 import BeautifulSoup
import csv
import requests

items = []

endpoints = f"https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9"

get_response = requests.get(endpoints)
soup = BeautifulSoup(get_response.content, 'lxml')

section = soup.find('tbody')
links = []

for tr in section.find_all('tr'):
    # for td in tr:
    #     for num in td:
    #         print(num)
    a_link = []
    for a in tr.find_all('a'):
        
        if 'href' in a.attrs:
            
            # item['hyper_link_for_novel'] = 
            a_link.append(a['href'])
            # print(a['href'])
    links.append(a_link)
# print(links)

for link in links:
    item = {}
    if bool(link):
        item['hyper_link_for_novel'] = f"https://ar.wikipedia.org{link[0]}"
        item['hyper_link_for_author'] = f"https://ar.wikipedia.org{link[1]}"
        item['hyper_link_for_country'] = f"https://ar.wikipedia.org{link[2]}"
        print(link[0])
    else:
        item['hyper_link_for_novel'] = "False"
        item['hyper_link_for_author'] = "False"
        item['hyper_link_for_country'] = "False"
    
    items.append(item)


filename = f'/home/naga/dev/scraping/best Arabic novels/hyperLinks.xlsx'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['hyper_link_for_novel','hyper_link_for_author','hyper_link_for_country'], extrasaction='ignore' , delimiter = ';')
    w.writeheader()
    # print(items)
    for item in items:
        w.writerow(item)
        print(item)

