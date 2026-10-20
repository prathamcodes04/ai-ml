# This file covers Python basics: print statements, variables, data types, keywords,
# comments, arithmetic and logical operators, type conversion, type casting,
# user input using input(), and practice problems using user input and comparisons.

# Basics
print("Hello World!", "Pratham is my name", "My age is 21")
print("Pratham is my name")
print("My age is 21")
print(23)

# Variable - is a name give to memory location in a program
name = "Pratham" 
age = 21
price = 25.99

age2 = age

print("My name is:", name)
print("My age is:", age2)

# Datatypes - integers, string, float, boolean, none (Primary Datatypes)
print(type(name))
print(type(age))
print(type(price))

# "" - msot prefered
name1 = "sk"
name2 = 'sk'
name3 = '''sk'''
print(name1, name2, name3)

# keywords - are reserved words in python (case sensitive)
# and, as, assert, break, class, continue, def, del, elif
# else, except, finally, False, for, from, global, if, import
# in, is, lambda, nonlocal, Non, not, or, pass, raise
# return, True, try, with, while, yield


# practice - sum of two numbers
# a = 2
# b = 3
# sum = a + b
print(sum)

# comments in python

# single line comment

'''
Multi Line
Comment
'''


# Operator - is a symbol that performs a certain operation betweem operands
'''
Arithmetic - + - * / % **
Relational/Compariosn - == != > < >= <=
Assignment - = += -= *= /= %= **=
Logical - not and or
'''

# a1 = 5
# b1 = 2
'''
print(a1 + b1)
print(a1 - b1)
print(a1 * b1)
print(a1 / b1)
print(a1 % b1) # remainder
print(a1 ** b1) # a^b
'''
val1 = False
val2 = True
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)


# Type conversion
# Two types of type conversion - types conversion and type casting
# Type conversion - python interpreter automatically does it
# Type casting - manually tell python to conv type1 variable to type2

# Type conversion
a = 2
b = 4.25
sum = a + b
print(sum)

# Type casting - to convert one data types to second data type
a1 = int("2") # type casting, we can use float("2") 
b1 = 4.25
print(type(a1))
print(a + b)


# Take input from user using input() statement
# name = input("Enter your name: ")
# print("Welcome", name)

# result of input() statement is always a string
# now to convert result into appropriate result we will use (type casting)
'''
int(input())
float(input())
'''

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# marks = float(input("Enter you marks: "))

# print("Welcome:", name)
# print("Age:", age)
# print("Marks:", marks)



# Practice question

# # wap to input 2 members and print their sum
# num1 = float(input("Enter num1: "))
# num2 = float(input("Enter num2: "))
# print("Sum:", num1 + num2)

# wap to input 2 numbers a & b, print true if a is greater is than or equal to b, if not print false
a = float(input("a: "))
b = float(input("b: "))
print(a >= b)
