
#----------------Task-2----------------------------------------------------

file=open('C:/Users/User/Desktop/Lab-1/matrix.txt')
eMpTy=''
for line in file:
    eMpTy+=line
spT=eMpTy.split('\n')
eE=[]
for i in range(len(spT)):
    eE.append(spT[i].split(' '))
nUM=[]
remove=0
for i in range(len(eE)):
    remove+= 1
    nUM.append([])
    for j in range(len(eE[i])):
        k=eE[i]
        if k[j]=='':
            break
        else:
            nUM[i].append(int(k[j]))     

tEmP1=[]
tEmP2=[]



mULt=False
count= 0
for l in nUM:
    count+=1
    if l==[]:
        mULt=True
        continue
    if mULt==False:
        tEmP1.append(l)
    else:
        tEmP2.append(l)

rEsuLT1=[]
for i in range(3):
    rEsuLT1.append([])
    for j in range(3):
        rEsuLT1[i].append(0)
lis= []
for i in range(len(tEmP1)):
    for j in range(len(tEmP2[0])):
        for k in range(len(tEmP2)):
            rEsuLT1[i][j] += tEmP1[i][k] * tEmP2[k][j]

fIlE=False

aA='' 
for r in rEsuLT1:
    aA+=' '.join(str(e) for e in r)
    aA+='\n'


rEsUlT_fiLe=open('C:/Users/User/Desktop/Lab-1/output4.txt','w')
rEsUlT_fiLe.write(aA[0:len(aA)-1])
file.close()
rEsUlT_fiLe.close()