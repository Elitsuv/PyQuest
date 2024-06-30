n = int(input("Enter the number"))
div = 0
for i in range (1, n):
    if (n % i == 0):
        div += i
if ( div == n):
    print("Hmm")
else: 
    print("No")