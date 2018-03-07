import csv
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

data = []
with open('sample_stocks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['returns'], row['dividendyield'])
        tup=(row['returns'],row['dividendyield'])
        data.append(tup)

for i in data:
    print(int(i[0]))

kmeans = KMeans(n_clusters=3, random_state=0).fit(data)
print('kmeans labels size: ',len(kmeans.labels_))
print(len(data))
print('kmeans labels: ', kmeans.labels_)

X1 = []
Y1 = []
X2 = []
Y2 = []
X0 = []
Y0 = []

for i in range(0,len(data)):
    if(kmeans.labels_[i]==1):
        X1.append(data[i][0])
        Y1.append(data[i][1])

for i in range(0,len(data)):
    if(kmeans.labels_[i]==0):
        X0.append(data[i][0])
        Y0.append(data[i][1])

for i in range(0,len(data)):
    if(kmeans.labels_[i]==2):
        X2.append(data[i][0])
        Y2.append(data[i][1])

for i in range(0,len(Y1)):
    print(X1[i])
    print(Y1[i])

print(len(X1))
print(len(X2))
print(len(X0))
#plt.plot(X1, Y1, 'ro')


plt.axis([-20, 50, 0, 5])
plt.show()