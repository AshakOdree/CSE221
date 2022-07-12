#task 1-----------------------------------------------------------
file_input=open('C:/Users/User/Desktop/lab-4/input-1.txt', 'r')
def Dijkstra(graph,source):
  dist={}
  dist[source]=0 
  prev={}
  q=[]
  for n in graph:
    if n!= source:
      dist[n]=float('inf')
    prev[n]=None
  for idx in range(1,len(graph)+1):
    q.append(idx)

  while len(q) != 0:
    up_b={}
    for v in q:
      up_b[v]=dist[v]
        
    e=min(up_b,key=up_b.get)
    q.remove(e)
    
    for var,w in graph[e].items():
      dist[var]=min(dist[var],dist[e]+w)
      prev[var]=e
  
  
  return dist

file1=open('C:/Users/User/Desktop/lab-4/output1.txt','w')

lines=''
for line in file_input:
    lines+=line
d=lines.split('\n')


counT=1
temp= int(d[0])
while temp !=0:
#for i in range(int(d[0])):
    v=[int(i) for i in d[counT].split(' ')]
    counT+=1
    edges={}
    for j in range(v[1]):
        m_line=[int(i) for i in d[counT].split(' ')]
        edges[(m_line[0],m_line[1])]=m_line[2]
        counT+=1
    nodes=[i for i in range(1,v[0]+1)]
    adjacency_Node={v:{} for v in nodes}
    
    for (u,v), w_uv in edges.items():
        adjacency_Node[u][v]=w_uv
        adjacency_Node[v][u]=w_uv

    titan=Dijkstra(adjacency_Node,1)
    file1.write('{}\n'.format(str(titan[nodes[-1]])))
    temp-=1
     
file_input.close()
file1.close()
