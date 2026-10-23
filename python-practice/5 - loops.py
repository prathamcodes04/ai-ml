

# loops - are used to repeat instruction

# while loops - runs untill condition is true

# count = 1 #iterator
# # while True: #infinite loop
# while count <= 5: #infinite loop
#     print("hello") #iteration
#     count += 1
    
# i = 1
# while i<= 8:
#     print("ok", i)
#     i += 1

# print number 1 - 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# print number 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# print multiplication table of number n
# i = 1
# n = 3
# while i <= 10:
#     print(n * i)
#     i += 1

# print elements of following list: [1,4,9,16,25,36,49,64,81,100]
# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

# searech for a number x in this tuple using loop:
# tuple = (1,4,9,16,25,36,49,64,81,100)
# i = 0
# while i < len(tuple):
#     if(tuple[i] == 100):
#         print("found at index:", i)
#     else:
#         print("finding...")
#     i += 1


# break and continue
# break - used to terminate the loop when condition becomes true
# continue - terminates execution in the currrent iteration and continues execution of the loop with the next iteration

# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# tuple = (1,4,9,16,25,36,49,64,81,100)
# i = 0
# while i < len(tuple):
#     if(tuple[i] == 25):
#         print("found at index:", i)
#         break
#     else:
#         print("finding...")
#     i += 1

# i = 1
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue #skips 3
#     print(i)
#     i += 1



# when we want to work on some iterator we use while loop
# when we need to traverse on some datatype we will use for loop

# loops - are used for sequential traversal
# for traversing list, string, tuples, etc

# nums = [1,2,3,4]
# veggies = ["potato", "tomato", "ladyfinger", "cucumber"]
# tup = (1,2,3,4,5)
str = "pratham"

# for val in nums:
# for val in veggies:
# for num in tup:
# for c in str:
#     print(c)

# for char in str:
#     if(char == 't'):
#         print("t found")
#         break
#     print(char)
# print("end")

# print element of the givven list using loop
# list = [1,4,9,16,25,36,49,64,81,100]
# for i in range(len(list)):
#     print(list[i])

# for i in range(10): #range(stop)
    # print(i)
    
# for i in range(2, 10): #range(start, stop)
    # print(i)
    
# for i in range(2, 10, 2): #range(start, stop, step)
    # print(i)
    
    
# linear search is used here

# print number 1 to 100
# for i in range(1, 101):
#     print(i)

# print numbers from 100 to 1
# for i in range(100, 0, -1): 
#     print(i)

# take input from user and give its multiplication
# num = int(input("Enter your number:"))
# for i in range(1, 11):
#     print(num * i)


# pass - is a null statment that does nothing
# it is used as a placeholder for future code
# for i in range(5):
#     pass
# print("boring work")



# wap to find sum of first n numbers using for loop
# n = 5
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print("total sum:", sum)

# n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)    

# wap to find factorial of firts n natural numbers
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)
