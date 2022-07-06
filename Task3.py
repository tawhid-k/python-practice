# brr = id
# arr = marks
def insertionSort(brr, arr):
    for i in range(len(arr)-1):
        j = i
        tmp = arr[j+1]
        tmpId = brr[j+1]
        while j >= 0:
            if arr[j]<tmp:
                arr[j+1] = arr[j]
                brr[j+1] = brr[j]
            else:
                break
            j = j-1
        arr[j+1] = tmp
        brr[j+1] = tmpId


my_file = open('input3.txt', 'r')
output_file = open('output3.txt', 'w')

n = int(my_file.readline())
brr = list(map(int, my_file.readline().split())) 
arr = list(map(int, my_file.readline().split())) 

insertionSort(brr, arr)

output_file.write(str(brr))
output_file.close()