import re

#1)
isOverall=False
while (isOverall==False):
    str1=str(input('Give a Password: '))
    lengthWord=int(len(str1))
    isSuccess = True;
    if((lengthWord>5) and (lengthWord<17)):
        print('Password Length success')
        isSuccess=False;
    else:
        print('Password Length failure')

    isNum = True;
    for letter in str1:
        if letter.isdigit():
            print ('Contains a number')
            isNum = False
            break

    if(isNum==True):
        print('Does not contain a number')

    isSpecial=True
    re.findall('[^A-Za-z0-9]',str1)
    if re.findall('[^A-Za-z0-9]',str1):
        print('Password contains a special character')
        isSpecial=False

    isCapital=True
    isLower = True
    for letter in str1:
        if(letter.islower()):
            isLower =False
        if letter.isupper():
            isCapital = False

    if(isCapital==False):
        print('Contains a uppercase')
    if(isLower==False):
        print('Contains a lowercase')

    if(isCapital==False and isLower==False and isSpecial==False and isNum==False and isSuccess==False):
        print('Good Password')
        isOverall=True
    isOverall=True


#2)
sentence = str(input('Give a sentence of words: '))

words = sentence.split()
sentLen = int(len(words))
if(sentLen==2 or sentLen==1):
    print('No middle words')
elif((sentLen%2)==0):
    print('Middle words: ',words[int(sentLen/2)-1],',and ',words[int(sentLen/2)])
else:
    print('Middle words: ', words[(int(sentLen / 2))])

#Longest Word
length = 0
longWord = ''
for t in words:
    if(len(t)>length):
        length = len(t)
        longWord = t
print('Longest word: ',longWord)

#Reverse sentence in words
words2 = []

for l in words:
    v = l
    y = list(v)
    newWord=''
    count = int(len(y))-1
    #print(len(y))
    for o in range(0,int(len(y))):
        #print(y[count])
        newWord=newWord + y[count]
        count=count-1
    #print(newWord)
    words2.append(newWord)

for w in words2:
    print(w)

#3)
input = [1,3,6,2,-1,2,8,-2,9]
int1=0
int2=1
int3=2
first=input[0]
second=input[1]
third=input[2]
collection = []
for d in input:
    for y in input:
        for o in input:
            if(not((d==y) or (d==o) or (o==y))):
                tuple = (d,y,o)
                collection.append(tuple)




for u in collection:
    l = u[0]+u[1]+u[2]
    if l==0:
        print (u)


print(len(collection))


print(words)
print(len(words))
d = len(words)
for q in words:
    print(q)

words2 = []

for l in words:
    v = l
    y = list(v)
    newWord=''
    count = int(len(y))-1
    print(len(y))
    for o in range(0,int(len(y))):
        print(y[count])
        newWord=newWord + y[count]
        count=count-1
    print(newWord)
    words2.append(newWord)

for w in words2:
    print(w)

str = "thi"
print ("Length of the string: ", len(str))
a = int(len(str))
print(a)
if((a>9) and (a<16)):
    print('success')
else:
    print('failure')

for letter in 'Python3':
    print('Current Letter: ', letter)
    if(letter.islower()):
        print (letter)
    if letter.isupper():
        break

for letter in 'Python3':
    print('Current Letter: ', letter)
    if(letter.islower()):
        print (letter)
    if letter.isdigit():
        print (letter)


#print special characters
s = 'Hellow123'
re.findall('[^A-Za-z0-9]',s)
if re.findall('[^A-Za-z0-9]',s):print(True)

line = 'My name is Charles Paul'
words = line.split()
print(words)
print(len(words))
d = len(words)
for q in words:
    print(q)

#Print word middle words
print (words[d-1])
print(words[0])

#Print word Backwords
words2 = []

for l in words:
    v = l
    y = list(v)
    newWord=''
    count = int(len(y))-1
    print(len(y))
    for o in range(0,int(len(y))):
        print(y[count])
        newWord=newWord + y[count]
        count=count-1
    print(newWord)
    words2.append(newWord)

for w in words2:
    print(w)

#Longest Word
length = 0
longWord = ''
for t in words:
    if(len(t)>length):
        length = len(t)
        longWord = t

print(longWord)
#Part 4
webApplications = ['Tony', 'Frank','Paul','Eddie','Brady','Blake']
python = ['Clark','Tony','Eddie','Harris']

same = []
different = []

isClear = True
for c in webApplications:
    for x in python:
        if(c==x):
            print(c)
            isClear=False
    if(isClear==False):
        same.append(c)
    else:
        different.append(c)
    isClear = True

for x in python:
    for c in webApplications:
        if(c==x):
            print(c)
            isClear=False
    if(isClear==True):
        different.append(x)
    isClear = True

for m in same:
    print(m)

for n in different:
    print(n)