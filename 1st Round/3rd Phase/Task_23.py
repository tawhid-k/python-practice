class Author:
    def __init__(self, name = None):
        self.name = name
        self.bookList = dict()
        
    def addBook (self, name, category):
        if self.name == None:
            print('A book can not be added without author name')
            return
        if category in self.bookList:
           self.bookList[category].append(name)
        if category not in self.bookList:
           self.bookList[category] = [name]
        
    def setName (self, name):
        self.name = name
        
    def printDetail(self):
        print('Number of Book(s): ' + str(len(self.bookList)))
        print('Author Name: ' + self.name)
        for i in self.bookList:
            print(i, end = ': ')
            for j in self.bookList[i]:
                print(j, end=', ')
            print()
            
a1 = Author()
print('=================================')
a1.addBook('Ice', 'Science Fiction')
print('=================================')
a1.setName('Anna Kavan')
a1.addBook('Ice', 'Science Fiction')
a1.printDetail()
print('=================================')
a2 = Author('Humayun Ahmed')
a2.addBook('Onnobhubon', 'Science Fiction')
a2.addBook('Megher Upor Bari', 'Horror')
print('=================================')
a2.printDetail()
a2.addBook('Ireena', 'Science Fiction')
print('=================================')
a2.printDetail()
print('=================================')

    