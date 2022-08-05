#Assignment 220 - Task 1
def shiftLeft(arr, k):
    n = len(arr)
    for i in range(n-k):
        arr[i] = arr[i+k]
    for i in range(n-k, n):
        arr[i] = 0
        
def rotateLeft(arr, k):
    n = len(arr)
    for j in range(k):
        firstVal = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = firstVal
        
def shiftRight(arr, k):
    n = len(arr)
    for i in range(n-1, k-1, -1):
        arr[i] = arr[i-k]
    for i in range(k):
        arr[i] = 0
        
def rotateRight(arr, k):
    n = len(arr)
    for j in range(k):
        lastVal = arr[n-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = lastVal

def remove(arr, n, idx):
    for i in range(idx, n):
        arr[i] = arr[i+1]
    arr[n-1] = 0
        
def removeAll(arr, n, elem):
    idx = 0
    for i in range(n):
        while i+idx < n and arr[i+idx] == elem:
            idx += 1
        if i+idx < n:
            arr[i] = arr[i+idx]
        else:
            arr[i] = 0
            
def splitting(arr, n):
    Sum = 0
    for i in arr:
        Sum += i
    leftSum = 0
    for i in arr:
        leftSum += i
        if leftSum == (Sum - leftSum):
            return True
    return False

def arraySeries(n):
    arr = []
    for j in range(1,n+1):
        for i in range(n-j):
            arr.append(0)
        for k in range(j, 0, -1):
            arr.append(k)
    return arr

def maxBunch(arr, n):
    curValue = arr[0] - 1
    maxRep = 0
    curRep = 0
    for i in arr:
        if i != curValue:
            maxRep = max(maxRep, curRep)
            curRep = 1
            curValue = i
        else:
            curRep += 1
    maxRep = max(maxRep, curRep)
    return maxRep

def repetition(arr):
    thisset = set()
    occ = []
    for i in arr:
        thisset.add(i)
    for i in thisset:
        counter = 0
        for j in arr:
            if j == i:
                counter += 1
        if counter in occ:
            return True
        elif counter > 1:
            occ.append(counter)
    return False
        
    
source=[10,20,30,40,50,60]
shiftLeft(source,3)
print(source)

source=[10,20,30,40,50,60]
rotateLeft(source,3)
print(source)

source=[10,20,30,40,50,60]
shiftRight(source,3)
print(source)

source=[10,20,30,40,50,60]
rotateRight(source,3)
print(source)

source=[10,20,30,40,50,0,0]
remove(source,5,2)
print(source)

source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)
print(source)

print(splitting([1, 1, 1, 2, 1], 5))

print(arraySeries(3))
print(arraySeries(4))

print(maxBunch([1,1,2, 2, 1, 1,1,1], 8))

print(repetition([4,5,6,6,4,3,6,4]))
print(repetition([3,4,6,3,4,7,4,6,8,6,6]))

print(splitting([1, 1, 1, 2, 1] , 5))
print(splitting( [2, 1, 1, 2, 1], 5))
print(splitting([10, 3, 1, 2, 10], 5))
