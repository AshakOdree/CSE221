#file 
fiLe_In=open('C:/Users/User/Desktop/Lab-2/input1.txt')
n=int(fiLe_In.readline())
lst=list(map(int,fiLe_In.readline().split()))

#shorting
def buBBleSorT(lst):
    for i in range(len(lst)-1):
        conDiTion=False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
            #swapting 
                conDiTion=True
                lst[j+1], lst[j]=lst[j], lst[j+1]
        if not conDiTion:
            break




fiLe_OuT=open('C:/Users/User/Desktop/Lab-2/output1.txt','w')
#tester
buBBleSorT(lst)
for i in lst: 
    fiLe_OuT.write(str(i)+' ')
fiLe_In.close()
fiLe_OuT.close()