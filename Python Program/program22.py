matrix =[      #it's a list in a list
    [1,2,3],
    [6,7,8]
]
#matrix[0][2]=10
#print(matrix[0][2])

#for row in matrix:  #print the same as input
    #print(row)

for row in matrix:
    for col in row:
        print(col)