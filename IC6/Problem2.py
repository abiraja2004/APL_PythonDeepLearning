import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, train_size=0.6, test_size=0.4)
gnb = GaussianNB()
#clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
trueTest = gnb.fit(X_train,y_train)
stats = trueTest.score(X_test, y_test)

predicted = cross_val_predict(trueTest, X_test, y_test, cv=10)
print('Result: ',metrics.accuracy_score(y_test,predicted))