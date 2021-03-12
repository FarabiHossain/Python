
#logical add

num1=int(input("Enter first number:"))
num2=int(input("Enter sceond number:"))
num3=int(input("enter third number:"))

if num1>num2 and num1>num3:
    print("max number is:",num1)
elif num2>num3 and num2>num1:
    print("max number is:",num2)
else:
    print("max number is:",num3)

#logical or

letter=input("Enter a letter:")

if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
    print("vowel")
else:
    print("consonent")