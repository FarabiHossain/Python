list=[10,20,30,40]
sum=0
for x in list:
    sum=sum+x
print(sum)

#1+2+3+4+5+6+7+....n
n=int(input("Enter the last number:"))
sum=0
for x in range(1,n+1,1):
    sum=sum+x
print(sum)
