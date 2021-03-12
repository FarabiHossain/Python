
#debugging:

def add(*adding):
    sum = 0
    for x in adding:
        sum = sum + x
        return sum

result = add(20,10,20,30)
print(result)