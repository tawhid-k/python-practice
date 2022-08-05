def partition(arr, p, q):
    x = arr[p]
    i = p
    print("Index: " + str(p) + " to " + str(q))
    print("Pivot " + str(arr[p]))
    for xoo in range(p, q+1, 1):
        print(arr[xoo], end=' ')
    print()
    for j in range(p+1, q+1):
        if arr[j] <= x:
            i=i+1
            print(arr[i], arr[j])
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[i] = arr[i], arr[p]
    for xoo in range(p, q+1, 1):
        print(arr[xoo], end=' ')
    print()
    return i

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)


my_file = open('input5.txt', 'r')
#output_file = open('output5.txt', 'w')

n = int(my_file.readline())
arr = list(map(int, my_file.readline().split())) 

quickSort(arr, 0, n-1)

print(arr)
#output_file.write(str(arr))
#output_file.close()