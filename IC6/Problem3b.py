import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from scipy.spatial.distance import cdist

stocks=pd.read_csv("sample_stocks.csv")

distortions = []
K = range(1,10)
for k in K:
    kmean = KMeans(n_clusters=k).fit(stocks)
    kmean.fit(stocks)
    distortions.append(sum(np.min(cdist(stocks, kmean.cluster_centers_, 'euclidean'), axis=1)) / stocks.shape[0])

plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()