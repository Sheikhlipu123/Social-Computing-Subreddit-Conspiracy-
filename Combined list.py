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
for c in extracted:
    c = "{0.scheme}://{0.netloc}/".format(urlsplit(c))
    c = c.replace("http://www.","")
    c = c.replace("https://www.","")
    c = c.replace("https://","")
    c = c.replace("http://","")
    if c in dict :
        dict[c]+=1
    else :
        dict[c]=1;
sorted_x = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)

myFile = open('csv.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile,lineterminator='\n')
   writer.writerow(extracted)
print(sorted_x)  
print(count)
print(total)





                            