def selectionSort(arr):
    for i in range(len(arr)-1):
        pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[pos]:
                pos = j
        cur = arr[i]
        arr[i] = arr[pos]
        arr[pos] = cur

my_file = open('input2.txt', 'r')
output_file = open('output2.txt', 'w')

n = int(my_file.readline())
m = int(my_file.readline())
arr = list(map(int, my_file.readline().split())) 

selectionSort(arr)

for i in range(m):
    output_file.write(str(i) + " ")

output_file.close()
