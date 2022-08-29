def findMin(arr, i, r):
    pos = i-1
    for j in range(i, r):
        if arr[j] < arr[pos]:
            pos = j
    return pos

def selectionSort(arr, i, n):
    if i == n:
        return
    else:
        pos = findMin(arr, i+1, n)
        cur = arr[i]
        arr[i] = arr[pos]
        arr[pos] = cur
        selectionSort(arr, i+1, n)

my_file = open('input1.txt', 'r')
#output_file = open('output2.txt', 'w')

n = int(my_file.readline())
arr = list(map(int, my_file.readline().split())) 

print(arr)
selectionSort(arr, 0, n)
print(arr)
