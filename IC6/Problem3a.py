# Implement K means clustering using scikit library
# read data using pandas library
# plot the result
# how you choose the correct parameter of K?

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

stocks=pd.read_csv("sample_stocks.csv")
kmeans=KMeans(n_clusters=3)
kmeans.fit(stocks)

# pull centroids and labels information from Kmeans on z
centroids=kmeans.cluster_centers_
labels=kmeans.labels_

colors = ['g.','r.','c.','y.','b.','o']

#plot the individual data points based on the label assigned by Kmeans
for i in range(len(stocks)):
    plt.plot(stocks.loc[i,"returns"],stocks.loc[i,"dividendyield"],colors[labels[i]], markersize = 3)

#plot the centroids
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()