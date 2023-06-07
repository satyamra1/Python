# Open the text file in write mode
with open("gla.txt", "a") as file:
    # Iterate through the range from 1000 to 9999
    for num in range(1000, 10000):
        # Convert the number to a string for easier manipulation
        num_str = str(num)
        # Check if the reversed string is equal to the original string
        if num_str == num_str[::-1]:
            # Write the palindrome number to the text file
            file.write(str(num) + "\n")
            print(file)