# Extract the following web URL text using BeautifulSoup
# https://en.wikipedia.org/wiki/Python_(programming_language)
# 2.Save it in input.txt
# 3.Applythe following on the text and show output:
# Tokenization
# Stemming
# POS
# Lemmatization
# Trigram
# Named Entity Recognition

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
from nltk import pos_tag, ne_chunk

res=requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup=bs4.BeautifulSoup(res.text,"html.parser")
#input=open('input.txt','w')
text=soup.select('p')
cars = []
#for text1 in text:
#input.write(text1.text +'\n')
#    print(text1.text)
#input.close()
a=open('input.txt')
input=a.read()
output = open('output.txt','w')

print('Tokenizing')
# tokenizing words
tokens=word_tokenize(input)
for i in tokens:
    output.write(i)
    output.write('\n')
#print(tokens)

print('Stemming')
output.write('STEMMING..................................................................................................................................')
output.write('\n')
# stemming
ps=PorterStemmer()
Stems=[]
for word in tokens:
    Stems.append(ps.stem(word))
#print(Stems)
for i in Stems:
    output.write(i)
    output.write('\n')

print('Parts of Speech')
output.write('PARTS OF SPEECH..........................................................................................................................')
output.write('\n')
# parts of speech tagging
POS=nltk.pos_tag(tokens)
#print(POS)
for i in POS:
    output.write(i[0]+',' + i[1])
    output.write('\n')

#print('Lemmatization')
output.write('Lemmatization..........................................................................................................................')
output.write('\n')
# lemmitazation
lem=WordNetLemmatizer()
lem_words=[]
for word in tokens:
    if lem.lemmatize(word, 'n') != word:
        lem_words.append(lem.lemmatize(word,'n'))
    elif lem.lemmatize(word, 'v') != word:
        lem_words.append(lem.lemmatize(word, 'v'))
    else:
        lem_words.append(word)
 #   print(lem_words)
for i in lem_words:
    output.write(i)
    output.write('\n')

#print('Trigrams')
output.write('Trigrams..........................................................................................................................')
output.write('\n')
# Trigrams
trigrams=[]
for i in range(len(tokens)):
    trigrams.append(tokens[i:i+3])
#print(trigrams)
for i in trigrams:
    for j in i:
        output.write(j + ',')
    output.write('\n')

print('Named Entity Recognition')
output.write('Named Entity Recognition..........................................................................................................................')
output.write('\n')
# Named Entity Recognition
NER=nltk.ne_chunk(POS)
print(NER)
#output.write(i)
#output.write('\n')