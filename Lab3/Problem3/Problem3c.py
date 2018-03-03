from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('cooking', pos='v'))
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

results = []
with open('textFile') as inputfile:
    for line in inputfile:
        q = word_tokenize(line)
        for t in q:
            results.append(t)
print(results)

for d in results:
    print(lemmatizer.lemmatize(d, pos='v'))
    print(d)