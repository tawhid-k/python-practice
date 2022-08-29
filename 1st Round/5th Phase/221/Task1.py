my_file = open('input1.txt', 'r')
output_file = open('output1.txt', 'w')
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
                if dis[v[0]] > (minDis + v[1]):
                    dis[v[0]] = (minDis+v[1])
                    
        
    edges = []

    for i in range(m):
        x, y, w = map(int, my_file.readline().split())
        edges.append([x, y, w])

    graph = dict()

    for i in range(1,n+1):
        lst = []
        for j in range(m):
            if edges[j][0] == i:
                lst.append([edges[j][1], edges[j][2]])
        graph[i] = lst
        
    dikstra(graph, 1)
    output_file.write(str(dis[n]) + '\n')

output_file.close()