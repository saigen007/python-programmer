a=int(input())
rev= 0
while(a > 0):
    reminder= a%10
    rev= (rev *10) + reminder
    a= a //10
print(rev)
