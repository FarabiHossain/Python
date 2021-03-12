#Returning value from function

def add(a,b):
    sum = a + b
    return sum

result = add(int(input("enter the value of A:")),int(input("enter the value of B:")))
print(result)

#max number finding:
def max(x,y):
    if x>y:
        return x
    else:
        return y

maximum = max(int(input("enter the value of A:")),int(input("enter the value of B:")))
print("The maximum Number is:",maximum)


#add string:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#If the number of arguments is unknown:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
