my_file = open('input1.txt', 'r')
output_file = open('output2.txt', 'w')
testCase = int(my_file.readline())

for t in range(testCase):

    n, m = map(int, my_file.readline().split())
    
    visited = [False] * (n+1)
    path = 0
    dis = [1e9] * (n+1)
    parent = [None] * (n+1)
    
    def dikstra(graph, source):
        dis[source] = 0
        curNode = 0
        for i in range(n):
            minDis = 1e9
            for j in range(1, n+1):
                if dis[j] < minDis and visited[j] == False:
                    minDis = dis[j]
                    curNode = j
            visited[curNode] = True
            for v in graph[curNode]:
                if dis[v[0]] > (minDis + v[1]):
                    dis[v[0]] = (minDis+v[1])   
                    parent[v[0]] = curNode
    
    def printPath(p):
        if parent[p] == p:
            output_file.write(str(parent[p]) + ' -> ')
            return
        printPath(parent[p])
        output_file.write(str(p) + ' -> ')
    edges = []
    
    for i in range(n+1):
        parent[i] = i
    for i in range(m):
        x, y, w = map(int, my_file.readline().split())
        edges.append([x, y, w])

    graph = dict()

    for i in range(n):
        lst = []
        for j in range(m):
            if edges[j][0] == i+1:
                lst.append([edges[j][1], edges[j][2]])
        graph[i+1] = lst
        
    dikstra(graph, 1)
    printPath(n)
    output_file.write('\n')

output_file.close()