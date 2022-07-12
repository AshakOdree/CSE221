def merge(A,p,q,r):
    tEmP1=q-p+1
    tEmP2=r-q
    leFT=[0]*(tEmP1)
    riGHt=[0]*(tEmP2)
    for i in range(1,tEmP1+1):
        leFT[i-1]=A[p+i-1]
    for j in range(1,tEmP2+1):
        riGHt[j-1]=A[q+j]
    i=0
    j=0
    for k in range(p,r+1):
        if i<tEmP1 and j<tEmP2:
            if leFT[i]<=riGHt[j]:
                A[k]=leFT[i]
                i+=1
            else:
                A[k]=riGHt[j]
                j+=1
        else:
            if i<tEmP1:
                A[k]=leFT[i]
                i+=1
            if j<tEmP2:
                A[k]=riGHt[j]
                j+=1
    

def mergesort(A,p,r):
    if p<r:
        q=(p+(r))//2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)
    return A


d1=open('C:/Users/User/Desktop/Lab-2/input4.txt', mode='r')
d2=open('C:/Users/User/Desktop/Lab-2/output4.txt', mode='w')
b1=d1.read().split('\n')
c=int(b1[0])
b2=b1[1].split(' ')
a=[]
for i in b2:
    i=int(i)
    a.append(i)
mergesort(a,0,c-1)
for i in a:d2.write(str(i)+' ')            