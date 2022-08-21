my_file = open('input1.txt', 'r')
n = int(my_file.readline())
m = int(my_file.readline())
visited = [False] * (n+1)
queue = []
path = []

def bfs(graph, start, end):
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        node = queue.pop(0)
        path.append(node)
        if node == end:
            break
        for i in graph[node]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
        

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
    
bfs(graph, 1, 12)
print(path)
