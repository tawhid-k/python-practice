my_file = open('input1.txt', 'r')
n = int(my_file.readline())
m = int(my_file.readline())

edges = []

for i in range(m):
    edge = list(map(int, my_file.readline().split())) 
    edges.append([edge[0], edge[1]])


print(n)
for i in range(n):
    print(i+1, end=" ")
    for j in range(m):
        if edges[j][0] == i+1:
            print(edges[j][1], end=" ")
    print()
    