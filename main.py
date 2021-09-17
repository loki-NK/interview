t = int(input("Enter the size of team:"))
k = int(input("Enter your number:"))
d = int(input("Enter number of days:"))
i= 0
j = 0
for i in range(1,d+1):
    j+=1
    if j==k:
        print(i)
    elif j==t:
        j=0
