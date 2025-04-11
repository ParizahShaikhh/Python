# Assignment 2: Pyramid Pattern
# Write a Python program to draw a pyramid of "*" using loops and string repetition.

# Example Output:
#     *
#    ***
#   *****
#  *******
# *********

# Guidelines:
# Use a loop to print each row of the pyramid.
# Center align the stars using spaces.
# You may use string multiplication (*) to repeat characters.



total_rows = 5

for i in range(1, total_rows + 1):
    stars = 2 * i - 1
    spaces = total_rows - i
    print(" " * spaces + "*" * stars)

    

# 🔁 Summary of the Process
# Decide how many rows you want (e.g., 5).

# Loop through each row from 1 to 5.

# For each row:

# Calculate spaces: total_rows - row_number

# Calculate stars: 2 * row_number - 1

# Print them together.


# Result:
#     *
#    ***
#   *****
#  *******
# *********
