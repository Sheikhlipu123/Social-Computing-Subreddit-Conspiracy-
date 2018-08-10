
import urllib.request
from bs4 import BeautifulSoup
import jsonlines
import json
extracted=[]
with jsonlines.open('ch.txt') as reader:
    for obj in reader:
        x=obj["url"]
        y=obj["is_self"];
        if y == "True" :
            extracted.append(x)
print("Extracted")

for url in extracted:   
    request = urllib.request.Request(url)
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html,'html.parser')
    main_table = soup.find("div",attrs={'id':'siteTable'})
    table = main_table.find_all("div",class_="md")
    for a in table:
        for tag in a.select('p a[href]'):
            all_links=tag['href']
            extracted.append(all_links)
            print(all_links)
            print("Done with")
with open('file.json', 'w') as f:
    json.dump(extracted,f,ensure_ascii=False)