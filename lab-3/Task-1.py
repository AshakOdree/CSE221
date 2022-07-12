file=open('C:/Users/User/Desktop/lab-3/input.txt')
c=''
for line in file:
    c+=line
d1=c.split('\n')

graph={}
for i in d1[1::]:
    c=i.split('\t')
    d=[]
    for j in c[1:]:
        d.append((j))
    if (c[0]) not in graph.keys():
        graph[(c[0])]=d
#print(graph)


file = open("C:/Users/User/Desktop/lab-3/output1.txt","w")
file = open("C:/Users/User/Desktop/lab-3/output1.txt","a")
for k,v in graph.items():
    file.write(k+"   ")
    for j in v:
        file.write(j+"   ")
    file.write("\n")
