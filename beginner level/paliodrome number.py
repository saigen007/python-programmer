a=int(input("enter a number: "))
temp=a
rev=0
while temp!=0:
    rev = (rev * 10) + (temp % 10)
    temp = temp // 10 
if a== rev:
    print("yes")
else:
    print("no")
