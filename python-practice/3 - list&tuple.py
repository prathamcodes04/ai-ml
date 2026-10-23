

# List - is a built-in data type that stores set of values (mutable)
# It can store elements of different types (integer, float, string, etc.)

marks = [87, 64, 55, 43, 22]
student = ["Karana", 85, "Delhi"]
print(student[0])
print(len(student))
print(len(student[0]))

# list is mutable
student[0] = "arjun"
print(student)

# list slicing similar to string slicing
# list_name[starting_index : ending_index]
print(marks[0:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

# list methods - append, sort, sort(reverse=True), reverse, insert
list = [2, 1, 3]
list.append(4) #mutating list
list.sort()
list.sort(reverse=True)
list.reverse()
list.insert(1, 8) #list.insert()
list.remove(1) #number mentioned to be removed
list.pop(2) #index mentioned to be removed
# print(list)

# tuples - built-in data type that lets us create immutable sequences of values
# includes slicing too
tup = (87, 64, 33, 95, 33)
print(tup[0])
# tup[0] = 3 #not allowed in python

'''
tup1 = ()
tup2 = (1,)
tup3 = (1,2,3)
'''

# tuple methods
print(tup.index(33)) #returns index of first occurence
print(tup.count(33)) # counts total occurences


# wap to ask the user to enter the names of their 3 favorite movies and store them in a list
# movies = []
# mov1 = input("Enter 1st movie: ")
# mov2 = input("Enter 2nd movie: ")
# mov3 = input("Enter 3rd movie: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# efficient way of solving above question
# movies = []
# for i in range(3):
#     movie = input(f"Enter {i + 1} movie: ")
#     movies.append(movie)
# print(movies)

# wap to check if a list contains a plaindrome of elements usnig copy()
# list = ["m", "a", "a", "m"]
# copy_list = list.copy()
# copy_list.reverse()
# if(copy_list == list):
#     print("palindrome")
# else:
#     print("not palindrome")

# wap to count the number of students with the "A" grade in the following tuple
# tuple = ("c", "d", "a", "a", "b", "b", "a")
tuple = ["c", "d", "a", "a", "b", "b", "a"]
print(tuple.count("a"))
# store the above values in a list and sort them from "a" to "d"
tuple.sort()
print(tuple)