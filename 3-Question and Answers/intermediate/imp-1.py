n = int(input("Enter number"))
if 1000 <= n <= 9999:
    print("Yes")
else:
    print("no")

while (n > 0):
    d = n%10
    ctr = 0
    for i in range (1, d+1):
        if (d%i == 0):
            ctr += 1
        if (ctr == 2):
            print("Prime")
        n = n//10