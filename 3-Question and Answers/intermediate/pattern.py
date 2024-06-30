for i in range(0,6):
    for j in range(0,i+1):
        print(j,end=" ")
    print()

#0
#01
#012
#0123
#01234

for i in range(1,6):
    for j in range(0,i+1):
        if(j%2==0):
            print("A",end=" ")
        else:
            print("B",end=" ")
    print()