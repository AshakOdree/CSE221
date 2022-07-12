file = open("C:/Users/User/Desktop/lab-3/input-4.txt","r")
line = file.readlines()
total_graph = int(line[0])
count = 1
def bsf_graph(visited, graph, node):
    queue.append(node)
    y=list(graph.keys())
    while queue:
        node = queue.pop()
        if node == y[-1]:
            break
        else:
            for items in graph[node]:
                if items not in visited:
                    visited.append(items)
                    queue.append(items)
                    d[items-1]=d[node-1]+1
    # print(d)
    return str(d[-1])

#i=0
while total_graph != 0:
#for i in range(total_graph):
    graph = {}
    value1, value2 = line[count].split()
    d = [0] * int(value1)
    visited = []
    queue = []
    #i+=1
    aA = int(value2)
    while aA !=0:
    #for j in range(int(value2)):
        count += 1
        x = line[count].split()
        total = [int(i) for i in x]
        graph[int(total[0])] = total[1::]
        p = total[1::]
        if p[0] not in graph:
            graph[p[0]] = [int(total[0])]
        else:
            graph[p[0]].append(total[0])
        aA-=1

    y = bsf_graph(visited, graph, 1)
    #file = open("C:/Users/User/Desktop/lab-3/output4.txt", "w")
    with open("C:/Users/User/Desktop/lab-3/output4.txt", "a") as file:
        file.writelines(str(y) + "\n")
    count += 1
    total_graph-=1

