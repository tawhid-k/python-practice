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
    i = -1
    j = n
    sum_forward = 0
    sum_backward = 0
    while i != j-1:
        if sum_forward <= sum_backward:
            i += 1
            sum_forward += arr[i]
        else:
            j -= 1
            sum_backward += arr[j]

    if sum_forward == sum_backward:
        return True
    else:
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
# 0 1 2 3 4 5 6 7