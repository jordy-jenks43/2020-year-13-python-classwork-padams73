''' This program demonstrates variables and inputs. '''

# variables can store one piece of information
# name them sensibly, use lower case and underscores between words (snakecase)
first_name = "John"

# We use format() to insert a variable where the curly braces are
print("Hello {} how are".format(first_name))

# we can do maths operations on variables that have numbers
number = 5
print(number*2)

# we use input() to get input from the user
# input should be assigned to a variable
name = input("What is your name?")

print("Greetings {}".format(name))

# by default, input() takes string (text) as input
# we can "cast" a variable, setting it to a data type
age = int(input("Enter your age:"))

print(age*2)
