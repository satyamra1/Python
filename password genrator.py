import random
import string

password_length = 12

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation
all_characters = uppercase_letters + lowercase_letters + numbers + symbols

uppercase_letter = random.choice(uppercase_letters)
lowercase_letter = random.choice(lowercase_letters)
number = random.choice(numbers)
symbol = random.choice(symbols)

remaining_characters = ''.join(random.choice(all_characters) for i in range(password_length - 4))

password = uppercase_letter + lowercase_letter + number + symbol + remaining_characters

print("Your secure password is:", password)
