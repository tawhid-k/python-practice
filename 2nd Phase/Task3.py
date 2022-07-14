my_file = open('input1.txt', 'r')
n = int(my_file.readline())
m = int(my_file.readline())

visited = [False] * (n+1)
path = []

def dfs(node, endPoint):
    if visited[endPoint] == True:
        return
    visited[node] = True
    path.append(node)

    for i in graph[node]:
        if visited[i] == False:
            dfs(i, endPoint)

def findPath(graph, endPoint):
    for i in range(1, n+1):
        if visited[i] == False and visited[endPoint] == False:
            dfs(i, endPoint)

edges = []

for i in range(m):
    edge = list(map(int, my_file.readline().split())) 
    edges.append([edge[0], edge[1]])

graph = dict()

for i in range(n):
    lst = []
    for j in range(m):
        if edges[j][0] == i+1:
            lst.append(edges[j][1])
    graph[i+1] = lst
    
findPath(graph, 12)
print(path)
