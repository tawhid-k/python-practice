my_file = open('input3.txt', 'r')
output_file = open('output3.txt', 'w')

n = int(my_file.readline())

arr = list(map(int, my_file.readline().split()))
s = my_file.readline()

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

idxJ = 0
idxj = 0
workJ = 0
workj = 0
seq = ''
j = []

for i in s:
    if i == 'J':
        workJ += arr[idxJ]
        seq += str(arr[idxJ])
        idxJ += 1
    elif i == 'j':
        idxj = idxJ - 1
        while arr[idxj] in j and idxj >= 0:
            idxj-=1
        if idxj >= 0:
            j.append(arr[idxj])
            seq += str(arr[idxj])
            workj += arr[idxj]
            
output_file.write(seq)
output_file.write('\nJack will work for ' + str(workJ) + ' hours')
output_file.write('\nJill will work for ' + str(workj) + ' hours')
