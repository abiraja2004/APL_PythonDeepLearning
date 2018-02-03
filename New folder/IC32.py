har = 'python program'
l={'a','e','i','o','u'}
total = 0
y=set()
a = list(har)
for k in a:
    #print(k)
    y.add(k)

d = (l & y)
print(d)

t = (d ^y)
print(t)
c=[]
for k in a:
    c.append(k)

y = len(d)
count=0
for p in c:
    if p in d:
        if count != y:
            count += 1
            total += 1
            c.remove(p)

print(c)

count=0
for p in c:
    if p in d:
        if count != y:
            count += 1
            total += 1
            c.remove(p)

print(c)
print(total)




