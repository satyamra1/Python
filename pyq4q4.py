# Input the list of numbers from the user
num_list = input("Enter the list of numbers (space-separated): ").split()
print(num_list)
# Convert the input string into a list of integers
num_list = list(map(float, num_list))
print(num_list)

# Use the filter() function to filter out even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, num_list))

# Print the filtered even numbers
print("Even numbers:", even_numbers)
