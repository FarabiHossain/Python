#set

num = {1,2,3,4,5,}  #it can't take repeted value
num1 = set([4,5,6,7,8])
#num.add(7)
#num1.remove(5)
print(num,num1)

print(num | num1)   # (|) union
print(num & num1)   #(&) intersection
print(num - num1)