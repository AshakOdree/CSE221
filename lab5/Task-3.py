
file_input=open('C:/Users/User/Desktop/lab5/input-3.txt', mode='r')
#f2=open('C:/Users/User/Desktop/lab5/output-3.txt', mode='w')
f=file_input.read().split('\n')
x=int(f[0])
n=f[1].split(' ')
lst=[]
for i in n:
    i=int(i)
    lst.append(i)

#shorting
j=f[2]
lst.sort()

#soducode
q=[]
jack_Hour=0
jill_Hour=0
sequence=''
index=0
for i in range(len(j)):
    if j[i]=='J':
        q.append(lst[index])
        jack_Hour+=lst[index]
        sequence+=str(lst[index])
        index+=1
    elif j[i]=='j':
        x=q.pop()
        jill_Hour+=x
        sequence+=str(x)
file_out=open('C:/Users/User/Desktop/lab5/output-3.txt','w')
file_out.write('{} \n'.format(sequence))
file_out.write('Jack will work for {} hours\n'.format(jack_Hour))
file_out.write('Jill will work for {} hours'.format(jill_Hour))
