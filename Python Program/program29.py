#xargs

def student(*details):   #now you can send lot of pera mitter
    print(details)

student(101,"farabi",102,"tahabi")

def add(*number):
    sum = 0
    for x in number:
        sum = sum + x
    print("The result is:",sum)

add(10,20,30,40)

#xxargs

def student(**studentinfo):  #** for key and value
    print(studentinfo)
    print(studentinfo["id"])

student(id=101,name="farabi")