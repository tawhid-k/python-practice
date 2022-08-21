my_file = open('input4.txt', 'r')
output_file = open('output4.txt', 'w')

n = 26
m = 18

visited = dict()
path = 0
nodes = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Motijheel', 'MOGHBAZAR']
dis = dict()
parent = dict()

def dikstra(graph, source):
    dis[source] = 0
    curNode = 0
    for i in nodes:
        minDis = 1e9
        for j in nodes:
            if dis[j] < minDis and visited[j] == False:
                minDis = dis[j]
                curNode = j
        visited[curNode] = True
        for v in graph[curNode]:
            if dis[v[0]] > (minDis + v[1]):
                dis[v[0]] = (minDis+v[1])   
                parent[v[0]] = curNode

for i in nodes:
    dis[i] = 1e9
for i in nodes:
    visited[i] = False

def printPath(p):
    if parent[p] == p:
        output_file.write(str(parent[p]) + ' -> ')
        return
    printPath(parent[p])
    output_file.write(str(p) + ' -> ')
edges = []

for i in nodes:
    parent[i] = i
for i in range(m):
    x, y, w = map(str, my_file.readline().split())
    edges.append([x, y, int(w)])

graph = dict()

for i in nodes:
    lst = []
    for j in range(m):
        if edges[j][0] == i:
            lst.append([edges[j][1], edges[j][2]])
    graph[i] = lst
    
dikstra(graph, 'Motijheel')
printPath('MOGHBAZAR')
output_file.write('\n')

output_file.close()