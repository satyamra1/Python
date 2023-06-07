'''def modify(lst):
    lst.remove(4)
    print(lst,id(lst))
lst =[1,2,3,4]
modify(lst)'''
#write a pyhon program to retrive key value and key value pair from a dictonary
'import math as mt'

'''print(mt.gcd(5,20,10))

ceil
floor

'''
'''import math 
n=1543665656
d=int(math.log10(n))+1
print(d)
import time
print(time.ctime())
a=[5,2,3,4]
a.sort()
print(a)'''
def convert_to_matrix(arr, rows, columns):
    if len(arr) != rows * columns:
        raise ValueError("Invalid array size")

    matrix = []
    index = 0

    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(arr[index])
            index += 1
        matrix.append(row)

    return matrix


# Example usage
array = [1, 2, 3, 4, 5, 6]
num_rows = 2
num_columns = 2

result = convert_to_matrix(array, num_rows, num_columns)
print(result)






