import jsonlines
import re
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import requests
import json
import operator
import csv
extracted=[]
count=0
total=0
dict={}
with jsonlines.open('ch.txt') as reader:
    for obj in reader:
        x=obj["selftext_html"]
        y=obj["is_self"];
        if y == "True" :
            soup = BeautifulSoup(x, 'lxml')
            table=soup.find_all('a')
            for b in table:
                url=b["href"]
                if not url.startswith('http'):
                    url = "https://reddit.com"+url
                url = url.replace("m.","")   
                url=url.replace("en.wikipedia","wikipedia")
                url = url.replace("youtu.be/","www.youtube.com/watch?v=")
                extracted.append(url)
                total+=1
        if y=="False" :
            url=obj["url"]
            url = url.replace("m.","") 
            url=url.replace("en.wikipedia","wikipedia")
            url = url.replace("youtu.be/","www.youtube.com/watch?v=")
            extracted.append(url)  

print("Done")
fin=[]
for x in extracted:
    if "zerohedge.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "www.rt.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "activistpost.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "theguardian.com/" in x or "guardian.co.uk/" in x or "theguardian.pe.ca/" in x:
        print(x)
        fin.append(x)
for x in extracted:
    if "infowars.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "nytimes.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "washingtonpost.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "globalresearch.ca/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "huffingtonpost.com/" in x or "huffingtonpost.co.uk/" in x or "huffingtonpost.ca/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "washingtonsblog.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "wikileaks.org/" in x or "wikileaks.com" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "naturalnews.com/" in x :
        print(x)
for x in extracted:
    if "reuters.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "independent.co.uk/" in x or "independent.ie" in x:
        print(x)
        fin.append(x)
for x in extracted:
    if "breitbart.com/" in x or "breitbart.tv" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "thelastamericanvagabond.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "telegraph.co.uk/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "blacklistednews.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "cnn.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "veteranstoday.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "alternet.org/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "foxnews.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "bloomberg.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "news.yahoo.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "businessinsider.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "whatsupic.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "sputniknews.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "beforeitsnews.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "thefreethoughtproject.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "salon.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "rawstory.com/" in x :
        print(x)
        fin.append(x)
for x in extracted:
    if "bbc.co.uk/" in x or "bbc.com/" in x:
        print(x)
        fin.append(x)
for x in extracted:
    if "therundownlive.com/" in x:
        print(x)
        fin.append(x)
for x in extracted:
    if "dailymail.co.uk/" in x:
        print(x)
        fin.append(x)

myFile = open('news.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile,lineterminator='\n')
   writer.writerow(fin)





                            