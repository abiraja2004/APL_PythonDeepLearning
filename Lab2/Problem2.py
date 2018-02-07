contact_list=[{"name":"Paul","number":"9134869697","email":"santosh@gmail.com"},
              {"name": "Tony", "number": "8169590423", "email": "king94@gmail.com"},
              {"name": "Kevin", "number": "18004522342", "email": "kingkevin95@yahoo.com"}]

def displayContacts(name):
    for i in contact_list:
        if((i["name"])==name):
            print(i)

isValid = False
while(isValid==False):
    value = input("Click on a value: ")
    if value=='a':
        print('a')
        choiceA = input('a) Name or b) Number')
        displayContacts(choiceA)
        isValid = True
    elif value=='b':
        print('b')
        isValid = True
    elif value=='c':
        print('c')
        isValid = True
    elif value=='d':
        print('d')
        isValid = True
    else:
        print('choose either a,b,c')




for i in contact_list:
    print(contact_list[0].get("name","none"))
    contact_list[0]["name"]="Adrian"

for i in contact_list:
    print(i)

