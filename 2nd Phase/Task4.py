my_file = open('input2.txt', 'r')
testCase = int(my_file.readline())

for t in range(testCase):

    n, m = map(int, my_file.readline().split())
    
    visited = [False] * (n+1)
    path = 0
    dis = [1e9] * (n+1)
    
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
                if dis[v] > (minDis + 1):
                    dis[v] = (minDis+1)
                    
        
    edges = []

    for i in range(m):
        x, y = map(int, my_file.readline().split())
        edges.append([x, y])
        edges.append([y, x])

    graph = dict()

    for i in range(n):
        lst = []
        for j in range(2*m):
            if edges[j][0] == i+1:
                lst.append(edges[j][1])
        graph[i+1] = lst
        
    dikstra(graph, 1)
    print(dis[n])