import pandas as pd
import csv

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()

print(iris.data)
print(iris.target)
print(iris.target_names)
print(iris.data[0][2])


mainData = []
with open('IXIC.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row1 = []
        print(row['Adj Close'], row['Volume'])
        row1.append(float(row['Open']))
        row1.append(float(row['High']))
        row1.append(float(row['Low']))
        row1.append(float(row['Close']))
        row1.append(float(row['Adj Close']))
        row1.append(float(row['Volume']))
        mainData.append(row1)


names2 = []
vars2 = []
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Good')
names2.append('Average')
names2.append('Average')
names2.append('Bad')
names2.append('Average')
names2.append('Average')
names2.append('Bad')
names2.append('Bad')
names2.append('Bad')
names2.append('Average')
names2.append('Average')
names2.append('Average')
names2.append('Average')
names2.append('Average')
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(0)
vars2.append(1)
vars2.append(1)
vars2.append(2)
vars2.append(1)
vars2.append(1)
vars2.append(2)
vars2.append(2)
vars2.append(2)
vars2.append(1)
vars2.append(1)
vars2.append(1)
vars2.append(1)
vars2.append(1)

print(mainData)
print(names2)

colors = ['navy', 'turquoise', 'darkorange']
lw = 2



lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(mainData, names2).transform(mainData)
print(X_r2)

for color, i, target_name in zip(colors, [0, 1, 2], vars2):
    plt.scatter(X_r2[names2 == i, 0], X_r2[names2 == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')

plt.show()