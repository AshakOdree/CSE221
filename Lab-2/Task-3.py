def insertionSort(aRR1,c,aRR2):
    for i in range(0,c-1):
        temP1=aRR2[i+1]
        temP2=aRR1[i+1]
        j= i
        while j >= 0:
            if aRR2[j]<temP1:
                aRR2[j+1]=aRR2[j]
                aRR1[j+1]=aRR1[j]
                j-=1
            else: break
        aRR2[j+1]=temP1
        aRR1[j+1]=temP2



fiLe_InT=open('C:/Users/User/Desktop/Lab-2/input3.txt', mode='r')
fiLe_OuT=open('C:/Users/User/Desktop/Lab-2/output3.txt', mode='w')
inTP1=fiLe_InT.read().split('\n')
inTp2=int(inTP1[0])
aRR1=inTP1[1].split(' ')
aRR2=inTP1[2].split(' ')
insertionSort(aRR1,inTp2,aRR2)        
for i in aRR1: fiLe_OuT.write(i+' ')