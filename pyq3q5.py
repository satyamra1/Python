#code to create toeplitz matrix
def matrix(elements):
    n = len(elements)
    t_matrix = [[elements[i - j] for j in range(n)] for i in range(n)]
    return t_matrix
elements = [1, 2, 3, 4, 5, 6]
t_matrix = matrix(elements)
for row in t_matrix:
    print(row)
    if matrix[i][j] != matrix[i-1][j-1]:
        print("not a t matrix")