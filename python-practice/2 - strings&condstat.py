# Topics Covered: Python Strings (creation, concatenation, length, indexing, slicing, negative indexing, escape sequences, and string methods) and Conditional Statements (if, elif, else, nested if-else). Practice programs: grading students, checking odd/even, finding the greatest of 3 numbers, and checking multiples of 7.


# strings - is a data types that stores a sequence of characters

# str1 = "this is a string" #most used
# str2 = 'this is a string'
# str3 = """this is a string"""

# escape sequence characters used for formating (\n - next line, \t - tab space)
# string1 = "This is a string.\n We are \t creating it in python"
# print(string1)

# basic operation
# concatenation - used to join two string using + symbol
str1, str2 = "Pratham ", "Gupta"
print(str1 + str2)

# length of string using len(), counts space too
print(len(str1))


# indexing - starts from 0 to ...., space is also given index too
name = "Pratham"
print(name[2])

# slicing accessing parts of a string
print(name[0 : 4])
print(name[0 : ]) #pthon automatically goes to end if last index not given
print(name[0 : len(name)]) #same output as above

# negative indexing goes from -1 to -2, -3, -4, .....
print(name[-4 : -1]) #ending index does not include so output is "tha"
print(name[ : -1]) 

# string functions

str = "i am studying python from Youtube"
print(str.endswith("ube")) #returns true if string ends with substr
print(str.capitalize()) #capitalizes 1st character
print(str.replace("o", "a")) #replace old value with new value
print(str.replace("python", "javascript")) #replace old value with new value
print(str.find("from")) #returns 1st index of 1st occurence
print(str.count("from")) #counts the occurrence of substr

# wap to input users first name and print its length
# name = input("Enter your first name: ")
# print("Length of your name is:", len(name))



# Conditional statements (if/elif/else)
# if - always checks
# elif - only check when if is false
# else - if all above conditions fails else with run

'''
light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
else:
    print("look")
print("End of the code")
'''

# grade students based on marks
# marks = float(input("Enter your marks: "))
# if(marks >= 90): grade = "A"
# elif(marks >= 80 and marks < 90): grade = "B"
# elif(marks >= 70 and marks < 80): grade = "C"
# else: grade = "D"
# print("Grade of the student: ", grade)

# nested loops
# age = 98
# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")


# wap to check if number entered by the user is odd or even
# num = int(input("Enter a number: "))
# if(num % 2 == 0): print("Even")
# else: print("Odd")

# wap to find greatest of 3 numbers enetred by the user
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))
# if(a > b and a > c): print(a)
# elif(b > c): print(b)
# else: print(c)

# wap to check if a numbr is a multiple of 7  not
num = int(input("Enter a number: "))
if(num % 7 == 0): print("Multiple of 7")
else: print("Not a multiple of 7")