import nltk
import requests
import bs4
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('words')
import re
from nltk import pos_tag, ne_chunk

a=open('input.txt')
input=a.read()
output = open('output.txt','w')

print('Tokenizing')
# tokenizing words
tokens=word_tokenize(input)
for i in tokens:
    output.write(i)
    output.write('\n')

#Based on IC7 problem
output.write('Lemmatization..........................................................................................................................')
output.write('\n')
# lemmitazation
lemEngine=WordNetLemmatizer()
lemArray=[]
for word in tokens:
    if (lemEngine.lemmatize(word, 'n')) != word:
        lemArray.append(lemEngine.lemmatize(word,'n'))
    elif lemEngine.lemmatize(word, 'v') != word:
        lemArray.append(lemEngine.lemmatize(word, 'v'))
    else:
        lemArray.append(word)
for i in lemArray:
    output.write(i)
    output.write('\n')


output.write('Bigrams..........................................................................................................................')
output.write('\n')
# Bigrams
BigramDict = {}
for i in range(len(tokens)):
    mainStr = tokens[i:i+2]
    value = ''
    for i in mainStr:
        value = value + i
        print(value)
    if value in BigramDict.keys():
        t = int(BigramDict.get(value))
        y = int(t + 1)
        BigramDict.update({value: y})
        #BigramDict.update(value : )
    else:
        BigramDict.update({value: 1})

print('Bigrams (All)')
print(BigramDict)
NewDict = {}
countMain = 0
mainVerb = ''
for i in BigramDict:
    if(BigramDict[i] > countMain):
        if re.match("^[a-zA-Z0-9_]*$", i):
            countMain = BigramDict[i]
            mainVerb = i
NewDict.update({mainVerb: countMain})
newVerb = countMain
countMain = 0
mainVerb = ''
for i in BigramDict:
    if(BigramDict[i] > countMain):
        if(BigramDict[i] < newVerb):
            if re.match("^[a-zA-Z0-9_]*$", i):
                countMain = BigramDict[i]
                mainVerb = i
NewDict.update({mainVerb: countMain})
newVerb = countMain
countMain = 0
mainVerb = ''
for i in BigramDict:
    if(BigramDict[i] > countMain):
        if(BigramDict[i] < newVerb):
            if re.match("^[a-zA-Z0-9_]*$", i):
                countMain = BigramDict[i]
                mainVerb = i
NewDict.update({mainVerb: countMain})
newVerb = countMain
countMain = 0
mainVerb = ''
for i in BigramDict:
    if(BigramDict[i] > countMain):
        if(BigramDict[i] < newVerb):
            if re.match("^[a-zA-Z0-9_]*$", i):
                countMain = BigramDict[i]
                mainVerb = i
NewDict.update({mainVerb: countMain})
newVerb = countMain
countMain = 0
mainVerb = ''
for i in BigramDict:
    if(BigramDict[i] > countMain):
        if(BigramDict[i] < newVerb):
            if re.match("^[a-zA-Z0-9_]*$", i):
                countMain = BigramDict[i]
                mainVerb = i
NewDict.update({mainVerb: countMain})
#print highest content bigrams (top 5)
print('Bigrams (Top 5)')
print(NewDict)

#open up input
a=open('input.txt')
input=str(a.read())
input = input.replace(' ','')


valuesMain = input.split('.')
containAll = []
for i in NewDict:
    for j in valuesMain:
        if(j.__contains__(i)):
            containAll.append(j)
#concatenated sentences
print('Concatenated sentences of bigrams: ')
for y in containAll:
    print(y)