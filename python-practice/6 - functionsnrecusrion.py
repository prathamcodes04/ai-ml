

# functions and recursion

# functions - are block statements that perform a specific task
# reduces redundant or repeatable code
# reduces redundancy

# def sum(a, b): #function_definition(param1, param2)
#     s = a + b
#     return s
# print(sum(2,3)) #function call; arguments
# print(sum(4,6))
# print(sum(5,8))

# wap to find average of three numbers
# def avg(a, b, c):
#     #we can also add loops, 
#     sum = a + b + c
#     avg = sum / 3
#     return avg
# print(avg(2,4,9,))


# types of function - built-in and user defined
# built-in functions - print(), len(), type(), range()
# user defined - built by users


# default paramters - assigning a default value to parameter, which is used when no argument is passsed
# default argument should be at last (b, a = 2)
# (a = 2, b) this is wrong
# def calc_prod(a, b = 2):
# # def calc_prod(a = 1, b = 2):
#     return a * b
# print(calc_prod(1))


# wap to print the lenth of the list
# print elements of a list in a single line
list = [1,2,3,4]
# def list_length(list):
#     print(len(list))
# list_length(list)

# print elements of a list in a single line
# def print_list(list):
#     for item in list:
#         print(item, end = " ")
# print_list(list)

# find factorial of n
# n = 5
# fact = 1
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(fact)
# factorial(n)  


#wap to convert usd to inr
# usd = 55
# def usdtoinr(usd):
#     inr = usd * 90
#     print(inr)
# usdtoinr(usd)  


#recursion - when a function call itself repeatedly 

# print n to 1 backwards 
# def show(n = 5):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1) 
# show(5)

# factorial
# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         # n! = (n - 1)! * n
#         return n * fact(n - 1)     
# print(fact(5))

# wap to calculate the sum of first n natural numbers
# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n - 1) + n
# sum = calc_sum(5)
# print(sum)

# wap to print all elements in a list

# def print_list(list, index):
#     if(index == len(list)):
#         return
#     print(list[index])
#     print_list(list, index + 1)
# print_list(list, 0)