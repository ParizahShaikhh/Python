# Assignment 4: Deductive Logic Game - Guess the Secret Number
# Write a Python program that implements a deductive logic game where the player must guess a secret three-digit number based on hints.

# Game Rules:
# The program generate a random three-digit secret number (e.g., "631").
# The player has 10 attempts to guess the secret number.
# After each guess, the program provides feedback:
# “Correct” or 👌 → A correct digit in the correct place.
# “Ok” or 👍 → A correct digit in the wrong place.
# “Wrong” or ❌ → No correct digits.
# The game ends if the player guesses correctly or exhausts all attempts.


# Example Interaction:

# Welcome to the Guessing Game!

# Guess a 3-digit number: 123
# ❌👍👍 or Wrong Ok Ok

# Guess a 3-digit number: 124
# ❌❌👍 or Wrong Wrong Ok

# Guess a 3-digit number: 561
# ❌👌👍 or Wrong Correct Ok

# Guess a 3-digit number: 671
# ❌👌👌 or Wrong Correct Correct

# Guess a 3-digit number: 981
# ❌❌👌 or Wrong Wrong Correct

# Guess a 3-digit number: 691
# ❌👌👌 or Wrong Correct Correct

# Guess a 3-digit number: 621
# ❌👌👌 or Wrong Correct Correct

# Guess a 3-digit number: 631
# 👌👌👌 or Correct Correct Correct or You Got IT
# ...


number = "631"
for i in range(1, 11):
    user = input("Guess the number: ")
    feedback = ""
    for i in range(3):
        
        if user[i] == number[i]:
            feedback += "👌"
        elif user[i] in number:
            feedback += "👍"
        else:
            feedback += "❌"
    print(feedback)
    if feedback == "👌👌👌":
        print("You got it!")
        break
else:
    print("Game Over. The secret number was 631")
    