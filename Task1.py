def bubbleSort(arr):
  sorted = True
  for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
          sorted = False
          break
  if sorted == True:
      return
  for i in range(len(arr)-1):
   for j in range(len(arr)-1-i):
    if arr[j] > arr[j+1]:
     arr[j], arr[j+1] = arr[j+1], arr[j]

#Initially it has been checked if the array is already sorted or not.
#If the array is sorted then the function will stop execution and return
#Thus it will work on O(N) for best case scenario

my_file = open('input1.txt', 'r')
output_file = open('output1.txt', 'w')

n = int(my_file.readline())
arr = list(map(int, my_file.readline().split())) 

bubbleSort(arr)

output_file.write(str(arr))
output_file.close()
