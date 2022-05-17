from bs4 import BeautifulSoup
import csv
import requests

links = []

endpoint = f"https://quranicaudio.com/"

get_response = requests.get(endpoint)
print(get_response.content)

soup = BeautifulSoup(get_response.content, 'lxml')
print(soup.prettify())

section = soup.find('div', {'class':'_21T051LFkHljITIXLg1R0J'})
print(section)

for li in section.find_all('li', attrs={'class':'_3WKKfenprs1hYlsRF-xOtp'}):
    links.append(li.a['href'])

print(links)  

# links = ['/quran/1', '/quran/2', '/quran/7', '/quran/8', '/quran/11', '/quran/15','/quran/19', '/quran/21', '/quran/37', '/quran/40', '/quran/44', '/quran/50', '/quran/55', '/quran/68', '/quran/72', '/quran/81', '/quran/106', '/quran/108', '/quran/109', '/quran/113', '/quran/115', '/quran/124', '/quran/125', '/quran/126', '/quran/127', '/quran/128', '/quran/135', '/quran/136', '/quran/158', '/quran/160', '/quran/74', '/quran/14', '/quran/134', '/quran/27', '/quran/64', '/quran/85', '/quran/28', '/quran/93', '/quran/103', '/quran/116', '/quran/9', '/quran/105', '/quran/161', '/quran/5', '/quran/6', '/quran/12', '/quran/26', '/quran/41', '/quran/53', '/quran/70', '/quran/71', '/quran/79', '/quran/88', '/quran/90', '/quran/91', '/quran/92', '/quran/107', '/quran/118', '/quran/119', '/quran/122', '/quran/129', '/quran/159', '/quran/10', '/quran/104', '/quran/4', '/quran/13', '/quran/17', '/quran/18', '/quran/20', '/quran/35', '/quran/43', '/quran/61', '/quran/80', '/quran/23', '/quran/130', '/quran/97']

for i in links:
    endpoint = f"https://quranicaudio.com{i}"
    
    get_response = requests.get(endpoint)

    soup = BeautifulSoup(get_response.content, 'lxml')

    if soup.find('div', {'class':'YuRhw1tjUohnA3r6u0TTU false'}):
        section_1 = soup.find('div', {'class':'YuRhw1tjUohnA3r6u0TTU false'})
    elif soup.find('div', {'class':'YuRhw1tjUohnA3r6u0TTU _2AcRl5L0LRlFXGHFWp962O'}):
        section_1 = soup.find('div', {'class':'YuRhw1tjUohnA3r6u0TTU _2AcRl5L0LRlFXGHFWp962O'})
    name = section_1.div.h1.text

    section_2 = soup.find('div', {'class':'RUtKwTYvwjlFGVwsr2c2Q'})

    items = []
    for li in section_2.find_all('li', attrs={'class':'list-group-item _3S_wx_oujN5yF0Tq6rbG-1'}):
        surat_name = li.find_all('span')
        surat_link = li.find_all('a')
        item = {}

        item['number'] = surat_name[2].text
        item['name'] = f"{surat_name[4].text} {surat_name[5].text}"

        item['read_surat_link'] = surat_link[1]['href']
        item['download_surat_link'] = surat_link[2]['href']

        item['surat_time'] = surat_name[10].text

        items.append(item)

        # print(surat_name[2].text)
        # print(surat_name[4].text)
        # print(surat_name[5].text)
        # print(surat_link[2]['href'])
        # print(surat_name[10].text)
        # print(li.div.div.div.div.h5.span.text)
        # print(li)

    filename = f'/home/naga/dev/scraping/quran/items/{name}.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['number','name','read_surat_link','download_surat_link', 'surat_time'], extrasaction='ignore' , delimiter = ';')
        w.writeheader()
        # print(items)
        for item in items:
            w.writerow(item)
            print(item)
