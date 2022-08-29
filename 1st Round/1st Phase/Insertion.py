def insertionSort(arr, i, n):
    if i == n-1:
        return
    else:
        j = i
        tmp = arr[j+1]
        while j >= 0:
            if arr[j]>tmp:
                arr[j+1] = arr[j]
            else:
                break
            j = j-1
        arr[j+1] = tmp
        insertionSort(arr, i+1, n)


my_file = open('input1.txt', 'r')

n = int(my_file.readline())
arr = list(map(int, my_file.readline().split())) 
print(arr)
insertionSort(arr, 0, n)
print(arr)
