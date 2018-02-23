import pandas as pd
import csv

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

iris = datasets.load_iris()
boston = datasets.load_boston()
iris_features = iris.data
iris_labels = iris.target
print(iris)
print(len(iris.target))
print(len(iris.data))
Features_train, Features_test, Labels_train, Labels_test = train_test_split(iris_features, iris_labels, test_size=0.2, train_size=0.8)
print(Features_train)
print(Features_test)
print(len(Features_train))
print(len(Features_test))

X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
clf = SVC()
clf.fit(Features_train, Labels_train)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='linear',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
for i in Features_test:
    print(clf.predict([[4.8, 3.4, 1.6, 0.2]]))

for i in range(0, len(Features_test)):
    print(Features_test[i])
    print(Labels_test[i])
    print(clf.predict([Features_test[i]]))


clf = SVC()
clf.fit(Features_train, Labels_train)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
for i in Features_test:
    print(clf.predict([[4.8, 3.4, 1.6, 0.2]]))

for i in range(0, len(Features_test)):
    print(Features_test[i])
    print(Labels_test[i])
    print(clf.predict([Features_test[i]]))