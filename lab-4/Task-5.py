from queue import PriorityQueue
import math
from collections import defaultdict 
grph=defaultdict(list)
def network(grph, src):
    pq = PriorityQueue()
    chk = [False]*len(grph)
    lst = [-math.inf]*len(grph)
    lst[source] = math.inf
    prev=[None]*len(grph)
    pq.put((-1*lst[src], src))
    while not pq.empty():
        c = pq.get()[1]
        if chk[c]: 
            continue
        chk[c] = True
        for d in grph[c]:
            alt = min(lst[c], d[1])
            if alt > lst[d[0]]:
                lst[d[0]] = alt
                prev[d[0]]=c
                pq.put((-1*lst[d[0]], d[0]))    
    lst=lst[1:]  
    f=[]
    for i in lst:
        if i==math.inf:
            i=0
            f.append(i)
        elif i==-math.inf:
            i=-1
            f.append(i)
        else: f.append(i)
    for i in f: 
        n2.write(str(i) + ' ')
    n2.write("\n")      
    
n1=open('C:/Users/User/Desktop/lab-4/input-5.txt', mode='r')
n2=open('C:/Users/User/Desktop/lab-4/output-5.txt',mode='w')
ln=n1.read().split('\n')
tc=int(ln[0])
z=1
while tc !=0:
    a=ln[z].split(' ')
    x=int(a[0])
    y=int(a[1])
    temp=0
    while temp <= x:
        grph[temp]
        temp+=1
    for k in range(z+1,y+z+1):
        b=ln[k].split(' ')
        d=int(b[1])
        c=int(b[0])
        e=int(b[2])
        xA=int(b[2])
        grph[c].append((d,e))   
    source=int(ln[z+y+1])
    network(grph,source)
    z+=y+2
    grph.clear()  
    tc-=1

