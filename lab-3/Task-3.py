
file = open("C:/Users/User/Desktop/lab-3/input.txt","r")
a=file.read().split("\n")
dict={}
nodes=a[0]
for i in a[1:]:
    li=i.split()
    dict[li[0]]=li[1:]

file2 = open("C:/Users/User/Desktop/lab-3/output3.txt", "w")


def DFS_VISIT(graph, node):
  visit[int(node)-1]=1
  printed.append(node)
  for j in graph[node]:
    if j not in visit :
      DFS_VISIT(graph, j)

def DFS(graph, endPoint):
  lst=[]
  flag=True
  for i in graph:
    if i  not in visit :
      DFS_VISIT (graph, i)
  
  for k in printed:
    if k not in lst :
      lst.append(k)
    else: 
      flag=False
      break
  file2.write('Places:')  
  for idx in lst:
    file2.write(' '+str(idx))
  file2.close()  

num_node=int(a[0])
visit=[0]*num_node
printed=[] 

DFS(dict, '12')