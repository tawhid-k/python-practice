my_file = open('input1.txt', 'r')
output_file = open('output1.txt', 'w')

tasks = []
n = int(my_file.readline())
for i in range(n):
    x, y = map(int, my_file.readline().split())
    tasks.append([x, y])

for i in range(n):
   for j in range(n-i-1):
       if tasks[j][1] > tasks[j+1][1]:
           tasks[j], tasks[j+1] = tasks[j+1], tasks[j]
           
done = []
f = 0
for i in tasks:
    if i[0] >= f:
        done.append(i)
        f = i[1]

output_file.write(str(len(done)))

for i in done:
    output_file.write('\n' + str(i[0]) + ' ' + str(i[1]))
