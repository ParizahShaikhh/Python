# print() is a funtion to display the text on the screen, ("") we put text in quotes so Python knows it's a message.
print("Hello World");
print("!!!");

# Variables and Data Types:
# Avariable is like a label/storage box that holds data. You can store numbers, text, or more complex information. You can put a name on the box and store whatever you want inside (Like: numbers, words, etc.).
name = "Parizah";
age = 1000;
# name is the variable, and "Parizah" is the data stored in it (a string).
# age is the variable, and 1000 is stored as a number (integer).
# Calling the variable name will display the data stored in it.
print(name);
print(age);

# Data Types:
# Python has several common data types:
#   - String (str): Text data (e.g., "Hello, World!")
#   - Integer (int): Whole numbers (e.g., 16 , 1000)
#   - Float (float): Decimal numbers (e.g., 3.14, 1.5)
#   - Boolean (bool): True or False
names = "Parizah";
ages = 1000;
print("Hello! My name is " + names + " and I am " + str(ages) + " years old.");
# Why Use str(ages)? Python doesn't allow you to directly mix numbers and text. str() converts the number to a string so it can be printed with the message.


# Integrating with Users - User Input in Python:
# In many programs, we need to take input from the user (e.g., asking for a name or a number). Python makes this easy with the input() function.
# 1. How to Use input():
name = input("What is your name? ");
print("Hello, " + name + "! Welcome to Python.");
# input("What is your name? "): Shows a prompt asking the user to type their name.
# Whatever the user types is stored in the variable name.
# we then use print() to display a personalized message.

# 2. Taking Multiple Inputs:
named = input("What is your name? ");
aged = input("How old are you? ");
print("Hi, " + named + "! You are " + aged + " years old.");

# 3. Important Tip: Converting Input to Numbers:
# The input() function always gives you a string. If you want to use numbers (for calculations), you'll need to convert the input using int() or float().
number = input("Enter a number: ");
number = int(number);
print("The number doubled is: " + str(number * 2));