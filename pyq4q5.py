import numpy as np
m = int(input("Enter the number of rows of the first matrix: "))
n = int(input("Enter the number of columns of the first matrix: "))
p = int(input("Enter the number of columns of the second matrix: "))

print("Enter the elements of the first matrix:")
matrix1 = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix1.append(row)
print("Enter the elements of the second matrix:")
matrix2 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)
result = np.matmul(matrix1, matrix2)
print("Result of matrix multiplication:")
print(result)
