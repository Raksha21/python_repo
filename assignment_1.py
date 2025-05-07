# Task 1 ------->

# Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
    
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division

# 3.  Displays the results of each operation on the screen.

a=input('Enter the first number: ')
b=input('Enter the second number: ')

a=int(a)
b=int(b)

# Addition
sum = a + b
print('Sum=',sum)

# Subtraction
sub = a - b
print('Sum=',sub)

# Multiplication
multiplication = a * b
print('Sum=',multiplication)

# Division
division = float(a / b)
print('Sum=',division)


# Task 2 ------->

# Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')

print('Hello, '+ firstName + ' ' + lastName + '! ' 'welcome to Python program.')
