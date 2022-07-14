def partition(arr, p, q):
    x = arr[p]
    i = p
    for j in range(p+1, q+1):
        if arr[j] <= x:
            i=i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    return i

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)


my_file = open('input5.txt', 'r')
output_file = open('output5.txt', 'w')

n = int(my_file.readline())
arr = list(map(int, my_file.readline().split())) 

quickSort(arr, 0, n-1)

output_file.write(str(arr))
output_file.close()