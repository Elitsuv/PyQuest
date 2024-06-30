n = int(input("Enter your number"))
ctr = 0
for i in range (1, n+1):
    if (n%i == 0):
        ctr += 1
if ctr == 2:
    print("No")
else:
    print("Yes its compo",n)
if (ctr == 0 or ctr == 1):
    print(n,"is Neither Prime nor composite")