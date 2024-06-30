n = int(input("Number: "))
ctr = 0

for i in range(1, n + 1):
    if n % i == 0:
        ctr += 1

if ctr == 2:
    print("Yes")
else:
    print("No")
