
# -*- coding: utf-8 -*-

import urllib.request
import pandas as pd
url = "https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9"

with urllib.request.urlopen(url) as i:
    html = i.read()
    
data = pd.read_html(html)[0]
print(data.head())
data.to_csv("/home/naga/dev/scraping/best Arabic novels/best_novels.xlsx")


    # items.append([tr])
    # tr_list = []
    # for td in tr:
    #     if td.span:
    #         print(td.span)


# # print(section)
# for tr in section.find_all('tr'):
#     # items.append([tr])
#     tr_list = []
#     for td in tr:
#         if td.span:
#             print(td.span)
        # elif td.span:
        #     print(td.span)
        # else:
        #     print('else')
            # tr_list.append(td.td)


    # items.append(tr_list) 
        # item = {}
        # item['الترتيب'] = td
    # items.append(li.div.div.div.text)
    # print(li.div.div.div.text)


# print(items)
# for i in items:
#     print(i[1])
#     print(i[3])
#     print(i[5])
#     print(i[7])
# filename = f'/home/naga/dev/scraping/quran/items/name.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f, fieldnames=['name', 'riwaya'], extrasaction='ignore' , delimiter = ';')
#     w.writeheader()
#     # print(items)
#     for item in items:
#         w.writerow(item)
#         print(item)



# # links = ['/quran/1', '/quran/2', '/quran/7', '/quran/8', '/quran/11', '/quran/15','/quran/19', '/quran/21', '/quran/37', '/quran/40', '/quran/44', '/quran/50', '/quran/55', '/quran/68', '/quran/72', '/quran/81', '/quran/106', '/quran/108', '/quran/109', '/quran/113', '/quran/115', '/quran/124', '/quran/125', '/quran/126', '/quran/127', '/quran/128', '/quran/135', '/quran/136', '/quran/158', '/quran/160', '/quran/74', '/quran/14', '/quran/134', '/quran/27', '/quran/64', '/quran/85', '/quran/28', '/quran/93', '/quran/103', '/quran/116', '/quran/9', '/quran/105', '/quran/161', '/quran/5', '/quran/6', '/quran/12', '/quran/26', '/quran/41', '/quran/53', '/quran/70', '/quran/71', '/quran/79', '/quran/88', '/quran/90', '/quran/91', '/quran/92', '/quran/107', '/quran/118', '/quran/119', '/quran/122', '/quran/129', '/quran/159', '/quran/10', '/quran/104', '/quran/4', '/quran/13', '/quran/17', '/quran/18', '/quran/20', '/quran/35', '/quran/43', '/quran/61', '/quran/80', '/quran/23', '/quran/130', '/quran/97']

# for i in links:
#     endpoint = f"https://quranicaudio.com{i}"
    
#     get_response = requests.get(endpoint)

#     soup = BeautifulSoup(get_response.content, 'lxml')

#     if soup.find('div', {'class':'YuRhw1tjUohnA3r6u0TTU false'}):
#         section_1 = soup.find('div', {'class':'YuRhw1tjUohnA3r6u0TTU false'})
#     elif soup.find('div', {'class':'YuRhw1tjUohnA3r6u0TTU _2AcRl5L0LRlFXGHFWp962O'}):
#         section_1 = soup.find('div', {'class':'YuRhw1tjUohnA3r6u0TTU _2AcRl5L0LRlFXGHFWp962O'})
#     name = section_1.div.h1.text

#     section_2 = soup.find('div', {'class':'RUtKwTYvwjlFGVwsr2c2Q'})

#     items = []
#     for li in section_2.find_all('li', attrs={'class':'list-group-item _3S_wx_oujN5yF0Tq6rbG-1'}):
#         surat_name = li.find_all('span')
#         surat_link = li.find_all('a')
#         item = {}

#         item['number'] = surat_name[2].text
#         item['name'] = f"{surat_name[4].text} {surat_name[5].text}"

#         item['read_surat_link'] = surat_link[1]['href']
#         item['download_surat_link'] = surat_link[2]['href']

#         item['surat_time'] = surat_name[10].text

#         items.append(item)

#         # print(surat_name[2].text)
#         # print(surat_name[4].text)
#         # print(surat_name[5].text)
#         # print(surat_link[2]['href'])
#         # print(surat_name[10].text)
#         # print(li.div.div.div.div.h5.span.text)
#         # print(li)

#     filename = f'/home/naga/dev/scraping/quran/items/{name}.csv'
#     with open(filename, 'w', newline='') as f:
#         w = csv.DictWriter(f, fieldnames=['number','name','read_surat_link','download_surat_link', 'surat_time'], extrasaction='ignore' , delimiter = ';')
#         w.writeheader()
#         # print(items)
#         for item in items:
#             w.writerow(item)
#             print(item)
