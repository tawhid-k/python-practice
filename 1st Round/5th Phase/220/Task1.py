#220 Task1 

class KeyIndex:
    def __init__(self, a):
        self.k = []
        for i in a:
            self.k.append(i)
            
    def search(self, val):
        for i in self.k:
            if i == val:
                return True
        return False
    
    def sort(self):
        n = len(self.k)
        for i in range(n):
            for j in range(n-1-i):
                if self.k[j] > self.k[j+1]:
                    self.k[j], self.k[j+1] = self.k[j+1], self.k[j]
        return self.k
    
class Tester:
    def __init__(self, a):
        self.a = a
        
    def searchTest(self):
        for i in self.a.k:
            if self.a.search(i) == False:
                return False
        return True
    
    def sortTest(self):
        for i in range(len(self.a.k) - 1):
            if self.a.k[i] > self.a.k[i+1]:
                return False
        return True
    
    def isCorrect(self):
        if self.searchTest() == True:
            print('Search method works properly')
        else:
            print('Search method is not working properly')
        self.a.sort()
        if self.sortTest() == True:
            print('Sort function works properly')
        else:
            print('Sort function does not work properly')
            
obj1 = KeyIndex([4,5,3,2,1])

print(obj1.search(3))

obj2 = Tester(obj1)

obj2.isCorrect()
        
        
    