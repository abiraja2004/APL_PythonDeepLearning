sentence = input('Give a sentence: ')
#sentence = 'hello world this is my first hello'
sent = sentence.split()
sent.sort()
mydict={}
for i in sent:
    if i in mydict:
        val = mydict.get(i,"none")
        mydict[i]=val+1
    else:
        mydict[i]=1


print(mydict)

