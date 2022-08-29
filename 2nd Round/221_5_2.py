my_file = open('input2.txt', 'r')
output_file = open('output2.txt', 'w')


tasks = []
n, m = map(int, my_file.readline().split())
for i in range(n):
    x, y = map(int, my_file.readline().split())
    tasks.append([x, y])

for i in range(n):
   for j in range(n-i-1):
       if tasks[j][1] > tasks[j+1][1]:
           tasks[j], tasks[j+1] = tasks[j+1], tasks[j]

people = [None] * m
done = 0
idx = 0

for i in tasks:
    for j in range(m):
        idx = (idx + j) % m
        if people[idx] == None:
            people[idx] = [i[0], i[1]]
            done += 1
            break
        elif people[idx] != None and people[idx][1] <= i[0]:
            people[idx].append([i[0], i[1]])
            done += 1
            break

output_file.write(str(done))
