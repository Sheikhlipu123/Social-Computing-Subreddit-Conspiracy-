import jsonlines
import re
from urllib.parse import urlsplit
import operator
import json
count=0
dict={}
with jsonlines.open('ch.txt') as reader:
    for obj in reader:
        x=obj["url"]
        x = "{0.scheme}://{0.netloc}/".format(urlsplit(x))
        x = x.replace("http://www.","")
        x = x.replace("https://www.","")
        x = x.replace("https://","")
        x = x.replace("http://","")
        print(x)
        count+=1
        if x in dict :
           dict[x]+=1
        else :
        	dict[x]=1;
sorted_x = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
print(sorted_x)
print(count)
with open('d.json', 'w') as f:
    json.dump(sorted_x,f,ensure_ascii=False)
print(len(dict))       