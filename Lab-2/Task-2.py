fiLe_In = open("C:/Users/User/Desktop/Lab-2/input2.txt",mode="r")
fiLe_In=[int(i) for i in fiLe_In.read().split()]
n=fiLe_In[0]

aRR=fiLe_In[2:]
mIN=aRR[0]

for i in range(len(aRR)-1):
    mIN=aRR[i+1]
    index = i+1
    for k in range(i,len(aRR)):
        if aRR[k]<mIN:
            mIN=aRR[k]
            index=k
    
    aRR[i], aRR[index] = aRR[index] , aRR[i]



fiLe_oUT =open("C:/Users/User/Desktop/Lab-2/output2.txt",mode= "w")
for i in range (fiLe_In[1]):
    fiLe_oUT.write(str(aRR[i])+" ")
