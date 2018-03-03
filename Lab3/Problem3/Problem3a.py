import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

results = []
with open('textFile') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))

print(results)


sentence = 'cats are fat and going to the mall and eating stuff is awesome'

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(sentence, pos="a"))