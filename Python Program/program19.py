"""
n=4
*
**
***
****
"""

n=4
for x in range(n+1):
    print(x*"0")

"""
n=4
*
***
*****
"""
n=4
for x in range(n+1):
    print((2*x-1)*"*")