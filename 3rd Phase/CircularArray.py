class CircularArray:
    def __init__(self,lin,st,sz):
        self.start = st
        self.size = sz
        self.cir = [None]*len(lin)
        k = self.start
        for i in range(len(lin)):
            if k == len(lin):
                k = 0
            self.cir[k] = lin[i]
            k += 1

    def printFullLinear(self):
        for i in range(len(self.cir)):
            print(self.cir[i], end=' ')
        print()

    def printForward(self):
        i = self.start
        for k in range(0,self.size):
            print(self.cir[i], end=' ')
            i = (i+1) % len(self.cir)
        print()
    def printBackward(self):
        k = (self.start + self.size-1) % len(self.cir)
        for i in range(0,self.size):
            print(self.cir[k], end=' ')
            k -= 1
            if k < 0:
                k = len(self.cir) - 1
        print()
    def resizeStartUnchanged(self, s):
        new_arr = [None] * s
        k = self.start
        l = k
        for i in range(len(self.cir)):
            new_arr[k] = self.cir[l]
            k += 1
            l += 1
            if k == s:
                k = 0
            if l == len(self.cir):
                l = 0
        self.cir = new_arr
    def linearize(self):
        arr = [None] * self.size
        k = self.start
        for i in range(self.size):
            if self.cir[k] != None:
              arr[i] = self.cir[k]
            k += 1
            if k == len(self.cir):
                k = 0
        self.cir = arr
    def palindromeCheck(self):
        arr = [None] * self.size
        k = self.start
        for i in range(self.size):
            if self.cir[k] != None:
              arr[i] = self.cir[k]
            k += 1
            if k == len(self.cir):
                k = 0
        j = self.size - 1
        for i in range(int(self.size/2)):
            if arr[i] != arr[j]:
                print('This array is not a palindorme')
                return
            j = j-1
        print('This array is a plaindrome')

    def sort(self):
        self.linearize()
        for i in range(len(self.cir)-1):
          for j in range(len(self.cir)-1-i):
            if self.cir[j] > self.cir[j+1]:
                self.cir[j], self.cir[j+1] = self.cir[j+1], self.cir[j]
        arr = []
        for i in range(len(self.cir)):
            arr.append(self.cir[i])
        k = self.start
        for i in range(len(self.cir)):
            self.cir[k] = arr[i]
            k += 1
            if k == len(self.cir):
                k = 0
    def equivalent(self, cir_arr):
        arr = [None] * self.size
        k = self.start
        for i in range(self.size):
            if self.cir[k] != None:
              arr[i] = self.cir[k]
            k += 1
            if k == len(self.cir):
                k = 0
        new_cir = [None]*cir_arr.size
        k = cir_arr.start
        j = 0
        for i in range(len(cir_arr.cir)):
            if cir_arr.cir[k] != None:
                new_cir[j] = cir_arr.cir[k]
            j += 1
            k = (k+1) % len(cir_arr.cir)
            
        if len(arr) == len(new_cir):
            for i in range(len(arr)):
                if arr[i] != new_cir[i]:
                    return False
        else:
            return False
        return True
    def intersection(self, c2):
        arr = []
        for i in range(len(self.cir)):
            for j in range(len(c2.cir)):
                if self.cir[i] == c2.cir[j] and self.cir[i] != None:
                    arr.append(c2.cir[j])
        return arr
    
lin_arr1 = [10, 20, 30, 40, None]
print("==========Test 1==========")
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.printForward() # This should print: 10, 20, 30, 40
c1.printBackward() # This should print: 40, 30, 20, 10
print("==========Test 2==========")
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40
print("==========Test 3==========")
lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None
print("==========Test 4==========")
lin_arr3 = [10, 20, 30, 20, 10, None, None]
c3 = CircularArray(lin_arr3, 3, 5)
c3.printForward() # This should print: 10, 20, 30, 20, 10
c3.palindromeCheck() # This should print: This array is a palindrome
print("==========Test 5==========")
lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome
print("==========Test 6==========")
lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50
print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30, None]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True
print("==========Test 8==========")
lin_arr7 = [10, 20, -30, 20, 50, 30, None, None, None]
c8 = CircularArray(lin_arr7, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c8.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c8)) # This should print: True
print("==========Test 9==========")
lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False
print("==========Test 10==========")
lin_arr9 = [10, 20, 30, 40, 50, None, None, None]
c10 = CircularArray(lin_arr9, 5, 5)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 7)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40