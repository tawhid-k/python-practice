def bubbleSort(arr, i, n):
    if i == n:
        return
    else:
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        bubbleSort(arr, i+1, n)

my_file = open('input1.txt', 'r')
#output_file = open('output1.txt', 'w')

n = int(my_file.readline()) # n = array size
arr = list(map(int, my_file.readline().split())) # Total array as input 

print(arr)
bubbleSort(arr, 0, n)
print(arr)
#output_file.write(str(arr))
#output_file.close()

