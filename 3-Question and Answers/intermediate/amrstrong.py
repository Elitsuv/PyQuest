n = int(input("Enter Your Number"))
s = 0
copy = n
while n > 0:
    d = n%10
    s += d**3
    n = n//10

if copy == s:
    print("yeh ha bhaoi")
else:
    print("sry")