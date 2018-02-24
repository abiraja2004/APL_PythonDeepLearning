import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_predict
from sklearn import metrics

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, train_size=0.5, test_size=0.5)
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
stats = clf.score(X_test, y_test)
print(stats)

predicted = cross_val_predict(clf, X_test, y_test, cv=10)
print(metrics.accuracy_score(y_test,predicted))