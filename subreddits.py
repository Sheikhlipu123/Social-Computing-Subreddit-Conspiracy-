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
            count+=1            
print("Done")
fin=[]
for x in extracted:
    if "reddit.com/r" in x :
        fin.append(x)
        x = x.replace("http://www.","")
        x = x.replace("https://www.","")
        x = x.replace("https://","")
        x = x.replace("http://","")
        m = re.search('r\/(.*?)\/',x)
        if m:
            x = m.group(1)
        if x in dict :
            dict[x]+=1
        else :
            dict[x]=1;
dict = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
print(dict)  
myFile = open('subreddits.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile,lineterminator='\n')
   writer.writerow(fin)
w = csv.writer(open("freqsubreddit.csv", "w"))
for key, val in dict:
    w.writerow([key, val])




                            