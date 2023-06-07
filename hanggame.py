import random

# Define a list of words for the game
words = ["python", "programming", "computer", "hangman", "game"]

# Select a random word from the list
word = random.choice(words)

# Create a list of underscores to represent the unknown letters in the word
display = ["_"] * len(word)

# Define the number of guesses the player has
max_guesses = 6
remaining_guesses = max_guesses

# Define a list to store the letters that the player has guessed
guessed_letters = []

# Define a function to display the current state of the game
def display_game():
    print(" ".join(display))
    print("Remaining guesses:", remaining_guesses)
    print("Guessed letters:", ", ".join(guessed_letters))

# Play the game until the player runs out of guesses or guesses the word correctly
while remaining_guesses > 0:
    display_game()

    # Prompt the player to enter a letter
    guess = input("Enter a letter: ").lower()

    # Check if the player has already guessed the letter
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Add the letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the letter is in the word
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Good guess!")
    else:
        print("Sorry, that letter is not in the word.")
        remaining_guesses -= 1

    # Check if the player has guessed the entire word
    if "_" not in display:
        print("Congratulations, you guessed the word:", word)
        break

# If the player runs out of guesses, end the game
if remaining_guesses == 0:
    print("Sorry, you ran out of guesses. The word was:", word)
