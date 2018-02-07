

class Book():
    def __init__(self):
        self.name = 'Default Title'
        self.pages = 100
        self.author = 'Default Author'

class Novel(Book):
    def __init__(self):
        super(Book, self).__init__()
        self.genre = 'Drama'
        self.hero = 'Hero'
        self.villan = 'Villain'
        self.plot = 'The hero wins'

class NonFiction(Book):
    _type = ''
    def __init__(self):
        super(Book, self).__init__()


    def setType(self,type):
        self._type=type

    def getType(self):
        print(self._type)

class Person():
    _name = ''
    def __init__(self):
        self._name = 'Name'

    def setName(self,name):
        self._name=name

    def getType(self):
        print(self._name)


class Student(Person):
    _checkedOut = []
    def __init__(self):
        super(Person, self).__init__()

    def checkOut(self, book):
        self._checkedOut.append(book)

    def getCheckOutLisk(self):
        return self._checkedOut

class Librarian(Person):
    def __init__(self):
        super(Person, self).__init__()

    def notifyLimit(self):
        print('Librarian: You have checked out limit of books')

class LibrarySystem:
    

bookShelf = []
newBook = Book()
newBook.name = 'Hunger Games'
newBook.pages = 350
bookShelf.append(newBook)
newBook = Book()
newBook.name = 'Game of Thrones'
newBook.pages = 600
bookShelf.append(newBook)
newBook = Novel()
newBook.genre
newBook.name='Game of Thrones Major'
newBook.pages = 655
newBook.author='George R.R Martin'
newBook.hero = 'Tyrion Lannister'
newBook.villain = 'Cersei Lannister'
newBook.plot = 'Game of Thrones is about a battle of 5 kingdoms and trying to get Iron Throne'
nfBook = NonFiction()
nfBook.name = 'The Bible'
nfBook.author = 'Various'
nfBook.pages = 900
nfBook.setType('Religious')
nfBook.getType()

newStudent = Student()
newStudent.checkOut(nfBook)
car = newStudent.getCheckOutLisk()
print(len(car))
for i in car:
    print(i.name)




