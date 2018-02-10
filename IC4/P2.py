import numpy as np

o = np.random.random((10,10))

print(o)

for i in o:
    count = 0
    for d in i:
        if(d > count):
            count = d
    print(count)