def LCS(a, b):
    x = len(a) + 1
    y = len(b) + 1
    w = []
    z = []
    for i in range(0, x):
        c = []
        d = []
        for j in range(0, y):
            c.append(0)
            d.append(None)
        w.append(c)
        z.append(d)
    for i in range(1, x):
        for j in range(1, y):
            if a[i - 1] == b[j - 1]:
                w[i][j] = w[i - 1][j - 1] + 1
                z[i][j] = 'diagonal'
            elif w[i - 1][j] >= w[i][j - 1]:
                w[i][j] = w[i - 1][j]
                z[i][j] = 'up'
            else:
                w[i][j] = w[i][j - 1]
                z[i][j] = 'left'
    # print(w)
    # print(z)
    prd = []
    p = x - 1
    q = y - 1
    while p >= 0 and q >= 0:
        if z[p][q] == 'diagonal':
            prd.append(b[p - 1])
            p -= 1
            q -= 1
        elif z[p][q] == 'up':
            p -= 1
        else:
            q -= 1
    prd.reverse()
    # print(prd)
    d = {"Y": "Yasnaya",
         "r": "Rozhok",
         "S": "School",
         "P": "Pochinki",
         "F": "Farm",
         "M": "Mylta",
         "H": "Shelter",
         "I": "Prison"}
    with open("C:/Users/User/Desktop/Lab-6/output-2.txt", "w") as file:
        for i in prd:
            if i in d.keys():
                # print(d[i])
                file.writelines(str(d[i]) + ' ')
        file.writelines("\n")
        file.write(str("Correctness of prediction: " + str(int((len(prd) * 100) / len(b))) + '%'))

f1 = open("C:/Users/User/Desktop/Lab-6/input-2.txt", "r")
l = f1.read().split("\n")
y = int(l[0])
a = l[1]
b = l[2]
LCS(a, b)
