my_file = open('input5.txt', 'r')
output_file = open('output5.txt', 'w')
testCase = int(my_file.readline())

for t in range(testCase):

    n, m = map(int, my_file.readline().split())
    
    visited = [False] * (n+1)
    path = 0
    dis = [-1] * (n+1)
    
    def dikstra(graph, source):
        dis[source] = 0
        curNode = source
        for i in range(n):
            minDis = -1
            for j in range(1, n+1):
                if dis[j] > minDis and visited[j] == False:
                    minDis = dis[j]
                    curNode = j
            if curNode in graph and visited[curNode] == False: 
                visited[curNode] = True
                for v in graph[curNode]:
                    if dis[v[0]] < v[1]:
                        dis[v[0]] = v[1]
                    
        
    edges = []

    for i in range(m):
        x, y, w = map(int, my_file.readline().split())
        edges.append([x, y, w])
        
    source = int(my_file.readline())
    graph = dict()

    for i in range(n):
        lst = []
        for j in range(m):
            if edges[j][0] == i+1:
                lst.append([edges[j][1], edges[j][2]])
        graph[i+1] = lst
    #if len(graph[source]) > 0:
        dikstra(graph, source)
        for i in range(1, n+1): 
           output_file.write(str(dis[i]) + ' ')
        output_file.write('\nIt is\n')
    #else:
    #    output_file.write('0\n')

output_file.close()