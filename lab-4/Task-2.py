
inpuT=open('C:/Users/User/Desktop/lab-4/input-1.txt')
ouTpuT=open('C:/Users/User/Desktop/lab-4/output-2.txt','w')

def Dijkstra(graph,source):
  dist={}
  dist[source]=0 
  prev={}
  q=[]
  for n in graph:
    if n!= source:
      dist[n]=float('inf')
    prev[n]=None
  for i in range(1,len(graph)+1):
    q.append(i)

  while len(q) != 0:
    up_b={}
    for v in q:
      up_b[v]=dist[v]
        
    e=min(up_b,key=up_b.get)
    q.remove(e)
    
    for var,w in graph[e].items():
      dist[var]=min(dist[var],dist[e]+w)
      prev[var]=e

  return prev

def serial(dic):
    key=[]
    value=[]
    for i,j in dic.items():
        key.append(i)
        value.append(j)
    if value[0]==None:
        return [key[0]]
    count=[list(dic.keys())[0]]
    count.append(dic[count[-1]])
    for i in range(len(dic)):         
        if count[-1]==list(dic.keys())[-1]:
            break
        else:
            c=key.index(count[-1])
            count.append(value[c])

    return count



lines=''
for line in inpuT:
    lines+=line
d=lines.split('\n')
# print(d)
count=1
temp = int(d[0])
while temp !=0:
#for i in range(int(d[0])):
    v=[int(i) for i in d[count].split(' ')]
    count+=1
    edges={}
    for j in range(v[1]):
        m_line=[int(i) for i in d[count].split(' ')]
        edges[(m_line[0],m_line[1])]=m_line[2]
        count+=1

    nodes=[i for i in range(1,v[0]+1)]
    adjacency_node={v:{} for v in nodes}
    
    for (u,v), w_uv in edges.items():
        adjacency_node[u][v]=w_uv
        adjacency_node[v][u]=w_uv

    path=Dijkstra(adjacency_node,1)

    lst=serial(path)
    ouTpuT.write(' '.join(str(e) for e in lst))
    ouTpuT.write('\n')
    temp-=1

    
inpuT.close()
ouTpuT.close()


