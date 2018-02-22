import pandas as pd
import csv

import matplotlib.pyplot as plt

from sklearn import datasets
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

mainData2 = []
names3=[]
vars3=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]


lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(mainData, vars2).transform(mainData)
print(X_r2)
x=[]
y=[]
for i in X_r2:
    print(i[0])
    x.append(i[0])
    y.append(i[1])
print(y)


for i in range(0, len(names2)):
    if names2[i] == 'Good':
        print('hi')
        print(x[i])
        red = x[i]
        x2.append(red)
        y2.append(y[i])

good = len(x2)
for i in range(0, len(names2)):
    if names2[i] == 'Average':
        print('hi')
        print(x[i])
        red = x[i]
        x3.append(red)
        y3.append(y[i])
        # y2.append[y[names2.index(i)]]
average = len(x2)
for i in range(0, len(names2)):
    if names2[i] == 'Bad':
        print('hi')
        print(x[i])
        red = x[i]
        x4.append(red)
        y4.append(y[i])
        # y2.append[y[names2.index(i)]]
bad = len(x2)
print('print I')
print(x2)
print(y2)

for i in range(0,len(x2)):
    plt.plot(x2, y2, 'ro')

for i in range(0,len(x3)):
    plt.plot(x3, y3, 'bo')

for i in range(0,len(x4)):
    plt.plot(x4, y4, 'go')

plt.axis([-5, 5, -2, 2])
plt.show()


# plt.plot(X_r2, 'ro')
# plt.axis([-2, 2, -5, 5])
# plt.show()

# for color, i, target_name in zip(colors, [0, 1, 2], vars2):
#     plt.scatter(X_r2[names2 == i, 0], X_r2[names2 == i, 1], alpha=.8, color=color,
#                 label=target_name)
# plt.legend(loc='best', shadow=False, scatterpoints=1)
# plt.title('LDA of IRIS dataset')
#
# plt.show()