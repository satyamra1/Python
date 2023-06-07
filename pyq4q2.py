num_list = input("Enter the list of numbers : ").split()
num_list = [int(num) for num in num_list]
s = [num**2 for num in num_list if num % 2 != 0]
print("Squared odd numbers:",s)
