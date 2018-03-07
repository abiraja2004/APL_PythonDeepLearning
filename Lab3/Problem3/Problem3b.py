import nltk
#nltk.download()
from nltk.corpus import wordnet as wn

#synsets = wn.synsets('phone')
#print([str(syns.definition) for syns in synsets])
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
s = 'Good muffins cost $3.88\nin New York. Please buy me two of them. \n\n Thanks.'
print(sent_tokenize(s))
print(word_tokenize(s))