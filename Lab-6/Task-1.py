#task-1
# n=int(input("Enter a number : "))
# n=int(input("Enter a number : "))
with open("C:/Users/User/Desktop/Lab-6/input-1.txt","r") as file:
    n=int(file.readline())

temp=""
if n <= 999:
    lst = [999] * (n + 1)
    lst[0] = 0
    for i in range(1, (n + 1)):
        for j in str(i):
            a = int(j)
            lst[i] = min(lst[i], lst[i - a] + 1)
    temp+=f'{lst[-1]}'
    # print(lst[-1])
else:
    # print("Please enter a number which range will be from 0 to 999.")
    temp+="Please enter a number which range will be from 0 to 999."
with open("C:/Users/User/Desktop/Lab-6/output-1.txt","w") as file:
    file.writelines(temp)
    



