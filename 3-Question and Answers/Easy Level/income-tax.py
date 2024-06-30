income = int(input("Enter Your Income:"))
if (income <= 100000):
    tax = 5/100*income + 100
elif income > 100000 and income < 500000:
    tax = 10/100*income + 100

else:
    tax = (20/100*income + 100)

    print("You Tax amnt", tax)