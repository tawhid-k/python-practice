my_file = open('dfs.txt', 'r')

topology = []

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            dfs(i)
    topology.append(node)

n = int(my_file.readline())
m = int(my_file.readline())

visited = [False] * (n+1)
edges = []

for i in range(m):
    edge = list(map(int, my_file.readline().split())) 
    edges.append([edge[0], edge[1]])

graph = dict()

for i in range(n):
    lst = []
    for j in range(m):
        if edges[j][0] == i:
            lst.append(edges[j][1])
    graph[i] = lst

dfs(0)

for i in range(len(topology)-1, -1, -1):
    print(topology[i], end=" ")
