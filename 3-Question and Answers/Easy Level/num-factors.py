data = int(input("Enter Number"))
for i in range (1, data+1):
    if (data % i == 0):
        print("Your Factorials", i)