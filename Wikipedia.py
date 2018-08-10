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
                print(url)
                total+=1
        if y=="False" :
            url=obj["url"]
            url = url.replace("m.","") 
            url=url.replace("en.wikipedia","wikipedia")
            url = url.replace("youtu.be/","www.youtube.com/watch?v=")
            extracted.append(url)
            print(url)         
print("Done")
fin=[]
for x in extracted:
    if "wikipedia.org" in x :
        print(x)
        fin.append(x)
        count+=1
myFile = open('wikipedia.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile,lineterminator='\n')
   writer.writerow(fin)
print(count)





                            