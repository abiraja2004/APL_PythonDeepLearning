import numpy as np
a = np.random.rand(15)
#print(20*a)
#print(a)
b=[]
for i in a:
    b.append(int(round(20*i)))

for i in b:
    print(i)

mydict = {}
for i in b:
    if i in mydict:
        val = mydict.get(i,"none")
        mydict[i]=val+1
    else:
        mydict[i]=1

print(mydict)

count = 0
longestNum = 0
for i in mydict:
    if(mydict[i]>=count):
        count = mydict[i]
        longestNum = i

print(longestNum)
