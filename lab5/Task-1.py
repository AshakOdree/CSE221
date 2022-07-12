#Task-1

file1=open("C:/Users/User/Desktop/lab5/input-1.txt", "r")
tem= file1.read()
#print(tem)
all_inpt =tem.split("\n")[1:]
#print(all_inpt)
new_list= []
for i in all_inpt:
  aA = i.split()
  start= aA[0]
  end=aA[1]
  new_list+=[[int(end),int(start)]]
#print(new_list)

#shorting
new_list.sort()
#print(new_list)



count= 1
end_time= new_list[0][1]


temP =str(new_list[0][1])
temP1=str(new_list[0][0])+"\n"
tasks=""
tasks+=temP+" "+temP1

for i in new_list[1:]:
  if  i[1] >= end_time:
    count+=1
    end_time= i[1]
    tasks+=str(i[1])+" "+str(i[0])+"\n"


tasks=str(count)+"\n"+tasks
with open('C:/Users/User/Desktop/lab5/output-1.txt', 'w') as file:
    file.write(tasks)
# file_out.close()


    
   