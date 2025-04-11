
      # Conditional Statements (if statements)

# Now that we know how to get input, let's learn how to make decisions in Python using 'if' statements.

# 1. What is an 'if' statement?
# An 'if' statement lets Python decide what to do based on conditions.

ifAge = int(input("Enter your age: "))

if ifAge >= 18:
      print("You're an adult!")
else:
      print("You're still a minor!")

# How it works:
# - If the age is 18 or more, it prints "You're an adult!"
# - Otherwise, it prints "You're still a minor!".

      # Now for the revision we will create simple programs:

# Write a program that asks for a number and checks if it's even or odd. (Hint: use 'number % 2 == 0 to check if a number is even.)
evenOdd = int(input("Enter a number: "))
if evenOdd % 2 == 0:
      print("The number is even!")
else:
      print("The number is odd!")


# Write a program that asks the user for their age and tells them if they're child (0-12), a teenager (13-19), or an adult(20+).
title = int(input("Enter your age: "))
if title <= 12:
      print("You are a child!")
elif title >= 13 and title <= 19:
      print("You are a teenager!")
else:
      print("you are an adult!")


      # 'if-elif-else' with Multiple Conditions

# Now that you understand 'if statements, let's introduce logical operators (and, or, not). These allow us to check multiple conditions at once.

      # 1. Checking for a Valid Age Range
validAge = int(input("Enter your age: ")) 

if validAge > 0 and validAge < 120:
      print("Your age is valid!")
else:
      print("Invalid age entered.")

      # 2. Checking if a Number is Positive, Negative, or Zero
      
num = int(input("Enter a number: "))

if num > 0:
      print("The number is positive.")
elif num < 0:
      print("The number is negative.")
else:
      print("The number is zero.")



      # Now for the revision we will create simple programs:

# 1. Write a program that asks the user for a temperature and checks if it's hot (above 30°C), cold (below 15°C), or moderate (between 15°C and 30°C).
temp = int(input("Enter temperature: "))
if temp > 30:
      print("The temperature is hot! 🔥")
elif temp > 15 and temp <= 30:
      print("The temperature is moderate. 😊")
else:
      print("The temperature is cold! ❄️")


# 2. Write a program that asks for a username and password. If the username is "admin" and the password is "977", print "Access Granted!", otherwise print "Access Denied!".
adminName = input("Enter your name: ")
adminPassword = int(input("Enter your password: "))

if adminName == "Parizah" and adminPassword == 977:
      print("Access Granted! ✅")
else:
      print("Access Denied! ❌")