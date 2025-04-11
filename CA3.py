# Assignment 3: Diamond Pattern
# Write a Python program to draw a diamond of "*" using loops and string repetition.

# Example Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# Guidelines:
# First, print the upper pyramid (similar to the previous assignment).
# Then, print the inverted pyramid below it.
# Ensure the diamond remains symmetric.

total_rows = 5
for i in range(1, total_rows + 1):
    spaces = total_rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
    


for i in range(total_rows - 1, 0, -1):
    spaces = total_rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


# Upper pyramid: i from 1 to total_rows
# Lower inverted pyramid: i from total_rows - 1 down to 1
