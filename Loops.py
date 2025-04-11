    # Loops (for & while loops)

# Loops help us repeat tasks without writing the same code over and over again. Imagine you have to print numbers from 1 to 100 - would you type each one manually? Nope! Loops handle this for us!

    # 1: The for Loop (Best for known Repetitions)

# A for loop is used when we know how many times we need to repeat a task.

# Example: Print numbers from 1 to 5:

for i in range(1, 6):
    print(i)
# range(1, 6) means start from 1 and go up to 5 (Python stops at 6).

# Example: Print each letter in a word:

word = "Python"
for letter in word:
    print(letter)



    # 1: The while Loop (Best for Unknown Repetitions)

# A while loop keeps running as long as a condition is True.

# Example: Keeps asking for a number until the user enters 0:
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): "))
# This will keep running until the user types 0.




    # Now for the revision we will create simple programs:

# Write a for loop that prints number from 10 to 1 (countdown).
for i in range(1, 11):
    print(i)



# Write a while loop that keeps asking for a password until the correct one (9078) is entered.
pass = int(input("Enter your password: "))
while pass != 9078:
    print("Incorrect password: ", pass)
    pass = int(input("Enter your password: "))