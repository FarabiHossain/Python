#gussing number

from random import randint
for x in range(1,5):
   gussingnumber=int(input("Enter a number from 1 to 5:"))
   randomnumber=randint(1,5)
   if gussingnumber==randomnumber:
       print("you won")
   else:
       print("you lose")
   print("random number is:",randomnumber)