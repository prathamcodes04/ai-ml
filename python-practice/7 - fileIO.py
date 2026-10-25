# file i/o in python

'''
- python can be used perform read n write operations on a file
- types of all files
    - text files: .txt, .docx, .log
    - binary files: .mp4, .mov, .png
- all data saved in the form of 0 and 1s 
'''


# file operations
'''
#open, read and close file operations

f = open("file_name", "mode")
- file_name can be sample.txt, demo.docx
- mode can be read or write mode

data  = f.read()

f.close()
'''

'''
# modes available
- r: open for reading
- w: open for writing, truncating the file first
- x: create new file and open it for writing
- a: open for writing, appending to the end of the file if it exists
- b: binary mode
- t: text mode
- +: open a disk file for updating
'''

# reading a file

# f = open("./python-practice/demo.txt", "r")
# # data = f.read()
# # data = f.read(5) #reads only starting five letters

# line1 = f.readline() #reads one line at a time
# print(line1)
# line2 = f.readline() #reads one line at a time
# print(line2)

# # print(data)
# # print(type(data))
# f.close()


# writing to a file
# f = open("./python-practice/demo.txt", "w")
# f = open("./python-practice/demo.txt", "a") #appending data instead of overwriting

# # f.write("I want to to js today") #this overwrite all data in the file
# f.write("\nGo with the flow") #appending data instead of overwriting use 'a' mode

# f.close()

# if we open a file in 'w' or 'a' mode and it does not exists python automatically creates a new file\
# f = open("./python-practice/sample.txt", "a")
# f.close()

# if we want to overwrite the starting of the file we use r+ mode
# f = open("./python-practice/sample.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close()

# w+ mode is used for reading n writing
# files gets truncated, fully wiped
# f = open("./python-practice/sample.txt", "w+")
# f.write("abc") #after wiping file abc will be saved in sample.txt
# print(f.read())
# f.close()

# # a+ mode places pointer at end then saves abc 
# f = open("./python-practice/sample.txt", "a+")
# print(f.read())
# f.write("abc") #after wiping file abc will be saved in sample.txt
# f.close()

# abc --> abcabc





'''
#summary
- r+ : read / overwrite / pointer at start / no truncate
- w+ : read / overwrite / pointer at start / truncate
- a+ : read / append / pointer at end / no truncate
'''



# with syntax - used to reduce above code
# better process
# no need to close file here as with automatically closses the file

# with open("./python-practice/demo.txt", "r") as f:
#     data = f.read()
#     print(data)
    
# with open("./python-practice/demo.txt", "w") as f:
#     f.write("new data")


# deleting a file - using os module
# module is a file written by another programmer that generally has a functions that we can use

# to install package we use: pip install tensorflow or if pip does not work it use pip3

# in os module we have a remove function

# import os
# os.remove("./python-practice/sample.txt")



# practice

# create a new file "practice.txt" and add given data 
with open("./python-practice/practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file i/o\n")
    f.write("using java\ni like programming in java\n")
    
# waf that replaces all occurences of "java" with "python" in above file
with open("./python-practice/practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("./python-practice/practice.txt", "w") as f:
    f.write(new_data)
    
# search if the work "learning" exists in the file or not using function
def check_for_word():
    with open("./python-practice/practice.txt", "r") as f:
        data = f.read()
        # if(data.find("learning") != -1):
        if("learning" in data):
            print("found")
        else:
            print("not found")
check_for_word()

# waf to find in which line of the file does the word "learning" occurs first, print -1 if not found
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("./python-practice/practice.txt", "r") as f:
        while data: #till data is valid
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_for_line()


# count even numbers from a file containing numbers seperated by comma
# find individual numbers --> parse/cast numbers substrings into integers
# string to list conversion we use split method without it we need to track commas run loop till data length, when we reach new comma it means num is read and then empty the string then check for eodd evenb

def count_even_nums():
    count = 0
    with open("./python-practice/test.txt", "r") as f:
        data = f.read()
        
        nums = data.split(",") #in the form of list
        # converting to int
        for val in nums:
            if(int(val) % 2 == 0):
                count += 1
        # print(nums)
        print(count)
count_even_nums()