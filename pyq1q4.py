#how do you create a list for a two dimentional matrix with 3 rows and four column with 0 values
'''n=3
m=4
val=[0]*n
for i in range(n):
    val[i] =[0]*m
print(val)
print('\n')'''

matrix=[]
print(matrix.append(3*[1]))
print(matrix.append(3*[1]))
print(matrix.append(3*[1]))
matrix[0][0]=2

print(matrix)