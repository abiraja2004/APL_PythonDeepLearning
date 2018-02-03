
import urllib.request
from bs4 import BeautifulSoup
import os
import pandas as pd

link ='https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
hi = urllib.request.urlopen(link)
parsedCode = BeautifulSoup(urllib.request.urlopen(link),"html.parser")
tableTags = parsedCode.find_all('table')
print(tableTags)

specificTable = parsedCode.find("table", {"class": "wikitable sortable plainrowheaders"})
print(specificTable)

u = specificTable.find_all('td')
k = specificTable.find_all('tr')
print(len(u))
print(len(k))

#Optional Panda stuff
df = pd.DataFrame()
#print(df)
o1 = []
o2 = []
o3 = []
o4 = []
o5 = []
o6 = []
for r in k:
    count = 0
    q=r.find_all('td')
    print(len(q))

    for col in q:
        count += 1
        #data=[col]
        if(count==1):
            o1.append(col.get_text())
        if(count==2):
            o2.append(col.get_text())
        if(count==3):
            o3.append(col.get_text())
        if(count==4):
            o4.append(col.get_text())
        if(count==5):
            o5.append(col.get_text())


    print(q)
data = {'Name':o1,'State':o2,'Administrative Capitals':o3,'Legislative Capitals':o4,'Year Capital Established':o5}
df = pd.DataFrame(data)
#for in u:
#    print(c)
print(df)
#g = []
#l = parsedCode.find_all('td')
#r = parsedCode.find_all('th')
#for x in l:
#    print(x)

#for y in r:
#    print(y)

#print()

#Optional Panda stuff
#df = pd.DataFrame(l)
#print(df)

#dr = pd.DataFrame(r)
#print(dr)