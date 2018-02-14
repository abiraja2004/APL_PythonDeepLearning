import numpy as np

o = np.random.randint(-10000,10000,(10,10))

print(o)

arrayMax = o.max(axis=1)
arrayMin = o.min(axis=1)

for i in range(10):
    print("Max: " + str(i) + ' max = ' + str(arrayMax[i]))

for i in range(10):
    print("Min: " + str(i) + ' min = ' + str(arrayMin[i]))