n = int(input("Enter the resersable no"))

A = n%10
n = n//10
B = n%10
n = n // 10
c = n

revserse = A*100 + B*10 + c
print("your number", revserse)