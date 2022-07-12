def Assignment_Selection(lst, x, y):
    lst.sort(key=lambda x: x[1])
    s = [False] * x
    c = 0
    i = 0
    while i != y:
        f = 0
        j = 0
        while j != x:
            if not s[j]:
                if lst[j][0] >= f:
                    c += 1
                    f = lst[j][1]
                    s[j] = True
            j+=1
        i += 1
    f2.write(str(c))


with open('C:/Users/User/Desktop/lab5/input-2.txt', mode='r') as f1:
    f = f1.read().split('\n')
f2 = open('C:/Users/User/Desktop/lab5/output-2.txt', mode='w')

z = f[0].split(' ')
x = int(z[0])
y = int(z[1])
lst = []
i = 1
while (i != len(f)):
    if f[i] == '':
        pass
    else:
        p = f[i].split(' ')
        q = []
        for j in p:
            r = int(j)
            q.append(r)
        lst.append(q)
    i += 1
#print(lst)
Assignment_Selection(lst, x, y)
