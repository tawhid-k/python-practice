def merge (arr, p, q, r):
    n1 = q-p+1
    n2 = r-q
    left = [None]*n1
    right = [None]*n2
    for i in range(n1):
        left[i] = arr[p+i]
    for i in range(n2):
        right[i] = arr[q+1+i]
    left.append(1e9)
    right.append(1e9)
    i = 0
    j = 0
    for k in range(p,r+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i+1
        else:
            arr[k] = right[j]
            j = j+1

def mergeSort(arr, p, r):
    if p < r:
        q = int((p+r)/2)
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        merge(arr, p, q, r)
        
my_file = open('input4.txt', 'r')
output_file = open('output4.txt', 'w')

n = int(my_file.readline())
arr = list(map(int, my_file.readline().split())) 

mergeSort(arr, 0, n-1)

output_file.write(str(arr))
output_file.close()