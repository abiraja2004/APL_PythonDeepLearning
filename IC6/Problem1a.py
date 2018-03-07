# In class exercise:
# Implementing Naive Bayes method using scikit-learn library
# use iris dataset available in the package
# Use cross validation to create training and testing part
# evaluate the model on testing part

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
import pprint as pp
import seaborn as sns
sns.set(color_codes=True)

iris=datasets.load_iris()

# write the iris data to a separate file
#iris_data=open('iris_data.txt', 'w')
#iris_data.write(iris['DESCR'])
#iris_data.write(pp.pformat(iris['target_names']))
#iris_data.write(pp.pformat(iris['data']))
#iris_data.write(pp.pformat(iris['target']))

gnb=GaussianNB()

X_train, X_test, y_train, y_test = train_test_split(
iris.data, iris.target, train_size=0.6,test_size=0.4)

y_pred=gnb.fit(X_train,y_train).predict(X_test)

count=0
for i in range(len(y_test)):
    print(y_test[i])
    print(y_pred[i])
    if y_test[i] != y_pred[i]:
        print('wrong')
        count+=1

print('Number of mislabeled points out of a total %d points : %d'
%(X_test.shape[0], count))