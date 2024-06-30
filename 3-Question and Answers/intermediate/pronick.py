# Example 2*3 = 6 ! 12 = 3*4

n = int(input("enter number"))
div = 0
for i in range (1, n+1):
    if (i * 1+1 == n):
        div = 1
        break
if div == 1:
    print("No its not")
