import numpy as np
import math
import matplotlib . pyplot as plt
import scipy as sc
x=[0,1,2,3,4,5,6,7,8,9]
y=[1,3,2,5,7,8,8,9,10,12]
yChange = []
meanX = sc.mean(x)
meanY = sc.mean(y)
print(meanX)
print(meanY)
t = (meanY/meanX)
print('t ',t)
for i in x:
    yChange.append((i*t)+y[0])
print(yChange)
print(y)
plt.plot(x, yChange)
plt.plot([x], [y], marker='o', markersize=3, color="red")
plt.show()

#x = np. linspace (0 , 10, 1000)
#y = np.power(x , 2)
#plt . plot (x , y)
#plt .show()
