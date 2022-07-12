def length(graph, u, v):  # M ...3
    l = graph[u]
    for node in l:
        if node[0] == v:
            return node[1]
    else:
        return None
def dijkstra(graph, source):
    dist[source] = 0
    q = [source]
    while len(q) != 0:
        u = q[0]
        q = q[1:]
        if visited[u]:
            continue
        visited[u] = True
        for v in graph[u]:
            v = v[0]  # 2, 4
            alt = dist[u] + length(graph, u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                if v not in q:
                    q.append(v)
                q.sort(key=lambda node: dist[node])
    
    return prev,dist


def print_path(prev, node):
    path = [node]
    while prev[node] is not None:
        path.append(prev[node])
        node = prev[node]
        if node=="Moghbazar":
            return path[::-1]



def prin(x,distance):
    file=open("C:/Users/User/Desktop/lab-4/output-4.txt", "a")
    #with open("C:/Users/User/Desktop/lab-4/output-4.txt", "a") as file:
    file.writelines(str("Shortest Path: ") + " ")
    for i in range(len(x)):
        file.writelines(str(x[i]) + " ")
    file.writelines("\n")
    file.writelines(str("Shortest Distance: ")+" "+str(distance) + " ")

file= open("C:/Users/User/Desktop/lab-4/input-4.txt")
line = file.readline()
no_of_test_cases = int(line)
while no_of_test_cases != 0:
    line = file.readline()
    graph = {}
    visited = {}
    dist = {}
    prev={}
    no_of_nodes, no_of_edges = [int(x) for x in line.split(" ")]
    while no_of_edges != 0:
        line = file.readline()
        u, v, d = [str(x) for x in line.split(" ")]
        d = int(d)
        if u not in graph.keys():
            graph[u] = [[v, d]]
            visited[u] = False
            dist[u] = 999
        else:
            graph[u].append([v, d])
        if v not in graph.keys():
            graph[v] = [[u, d]]
            visited[v] = False
            dist[v] = 999
        else:
            graph[v].append([u, d])
        no_of_edges-=1
    prev,distance = dijkstra(graph, "Moghbazar")
    x = print_path(prev, "Motijheel")
    dis=distance["Motijheel"]
    prin(x,dis)
    no_of_test_cases-=1
        