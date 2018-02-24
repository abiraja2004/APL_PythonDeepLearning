from nltk.stem import WordNetLemmatizer

results = []
with open('textFile') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))

print(results)


sentence = 'I am paul charles and i like to eat food'

lemmatizer = WordNetLemmatizer(sentence)
print(lemmatizer)