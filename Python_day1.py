#DAY-1
# 𝐏𝐫𝐢𝐧𝐭 𝐒𝐨𝐦𝐞 𝐕𝐚𝐥𝐮𝐞

# Write a program that prints "Hello, World!" to the console.
"""print("Hello, World!")"""

# Write a program that prints the sum of 15 and 25.
"""print(15+25)"""

# Write a program that prints your name and age.
"""a = "karthik"
b = 25
print(f"My name is {a} and my age is {b}")"""

# Write a program that prints the result of multiplying 7 by 8.
"""print(7*8)"""

# Write a program that prints the current year.
"""from datetime import datetime
a = datetime.now().year
b = datetime.now().month
c = datetime.now().day
d = datetime.now().date()
e = datetime.now().timestamp()
print(f"year is {a} and month is {b} and day is {c} and date is {d} and timestamp is {e}")"""


# Take Input from User

# Write a program that takes a user's name as input and prints a greeting message.
"""a = input("name:")
print(f"Hi {a}, I hope you are doing well")"""

# Write a program that takes two numbers as input and prints their sum.
"""a = int(input("enter value a:"))
b = int(input("enter value b:"))
print(a + b)"""

# Write a program that takes a string as input and prints it in uppercase.
"""a = input("enter the sentence:")
print(a.upper())"""

# Write a program that takes the user's age as input and prints a message saying how old they will be next year.
"""a = int(input("enter the age of person this year:"))
print(f"Next year the person age is {a+1}")"""

# Write a program that takes a user's city as input and prints a message saying "Hello from city!".
"""a = input("enter city:")
print(f"Hello from {a}")"""

# 𝐏𝐥𝐚𝐲 𝐰𝐢𝐭𝐡 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬

# Write a program that assigns the values 10, 20, and 30 to three variables and prints their sum.
"""a = 10
b = 20
c = 30
print(a+b+c)"""

# Write a program that swaps the values of two variables and prints the new values.
"""a = 10
b = 20
a,b = b,a
print(a,b)

#method - 2
c = 24
d = 23
temp = 0
temp = c
c = d
d = temp
print(c,d)"""

# Write a program that assigns your first name to one variable and your last name to another variable, then prints them together.
"""a = "Gattu"
b = "Karthik"
print(a+" "+b)
print(f"{a} {b}")"""

# Write a program that calculates the area of a rectangle with length 5 and width 10, and stores the result in a variable.
"""l = 5
b = 10
c = l*b
print(c)"""

# Write a program that initializes a variable with a value of 50, then adds 10 to it and prints the result.
"""a = 50
a = a + 10
print(a)"""


# 𝐂𝐚𝐬𝐭 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞
# Write a program that takes a string input of a number and converts it to an integer, then prints the integer.
"""a = "5"
print(type(a))
a = int(a)
print(type(a))
print(a)"""

# Write a program that takes a float number and casts it to an integer, then prints the integer.
"""a = 5.0
print(type(a))
a = int(a)
print(type(a))
print(a)"""

# Write a program that takes an integer and casts it to a float, then prints the float.
"""a = 5
print(type(a))
a = float(a)
print(type(a))
print(a)"""

# Write a program that takes an integer and converts it to a string, then prints the string.
"""a = 5
print(type(a))
a = str(a)
print(type(a))
print(a)"""

# Write a program that takes a Boolean value and casts it to an integer, then prints the integer value.
"""a = True
print(type(a))
a = int(a)
print(type(a))
print(a)"""
#for True it is 1 for false it is 0.

# 𝐎𝐮𝐭𝐩𝐮𝐭 𝐅𝐨𝐫𝐦𝐚𝐭𝐭𝐢𝐧𝐠
# Write a script to print the names of three fruits, each separated by a hyphen (-).
"""a = "mango"
b = "banana"
c = "papaya"
print(f"{a},{b},{c}")"""

# Create a script that takes a person's first name and last name, concatenates them with a space in between, and prints the result.
"""a= "Gattu"
b= "Karthik"
print(a + " " + b)
print(f"{a} {b}")"""

# Format and print a message showing a person's name and their score, with the score rounded to one decimal place.
"""a = "karthik"
b = 5.112
b = round(b,1)
print(f"{a} score is {b}")"""

# Write a script to print a table of items and their prices, with the item names left-aligned and the prices right-aligned.
"""items = ("mango",20),("banana",15)
for a in items:
    print(a)"""

# Print the numbers 1 through 5, each separated by a comma and a space.
"""for i in range(1, 6):
    if i < 5:
        print(i, end = ", ")
    else:
        print(i)"""
