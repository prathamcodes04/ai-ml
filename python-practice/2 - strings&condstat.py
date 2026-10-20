
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
