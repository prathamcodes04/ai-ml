
# Dictionaries - are used to store data values in key:value pairs
# they are unordered (no index), mutable and dont allow duplicate keys
# key values are string only

# dict = {
#     "name": "Pratham", 
#     "cgpa": 9.6,
#     "marks": [98, 75, 87],
#     "subjects": ["python", "c", "java"],
#     "topics": ("dict", "set"),
# }

# print(dict)
# print(type(dict))
# print(dict["name"])
# print(dict["cgpa"])
# print(dict["marks"])
# dict["cgpa"] = 9.9
# print(dict["cgpa"])

# adding key:value pair to a null dictionary
# null_dict = {}
# null_dict["name"] = "Pratham"
# print(null_dict)

# nested dictionaries
student = {
    "name": "Pratham",
    "score": {
        "chem": 98,
        "phy": 97,
        "math": 95
    }
}
# print(student["name"])
# print(student["score"])
# print(student["score"]["chem"])
# print(student["score"]["chem"])
# student["score"]["chem"] = 100;
# print(student["score"]["chem"])

# dictionary mehtods
# print(student.keys()) #returns all keys
# print(list(student.keys())) #returns all keys
# print(student.values()) #returns all values
# print(student.items()) #returns all (key, val) pairs as tuple
# print(student.get("score")) #returns key according to value
# student.update({"city" : "delhi"})
# print(student)


# set - is the collection of the unordered items
# each element in the set must be unique and immutable
# list and dictonaries cant be stored in set as they are mutable

nums = {1,2,3,4}
set2 = {1,2,2,2} #repeated elements stored only once, so it resolved to {1,2}
# null_set = set()

# collection = {1,2,2,3,4, "hello", "world", "world"}
# print(collection) #duplicate values get ignored
# print(type(collection))
# print(len(collection)) #ignores duplicate items

# collection = {} #this is a dictionary not a set
# print(type(collection))
# collection1 = set() #this is an empty set
# print(type(collection1))

# set = {1,2,3,4}

# set methods
# set.add(5)
# set.add("ok")
# set.add((1,2,3))
# set.add([1,2,3]) #cannot add list as it is a unhashable type means we can add immutable value as it has hash value but list is mutable and its hash values can
# set.remove(2)
# set.clear()
# set.pop()


# union and intersection
# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))


# practice
# dictionary = {
#     "table": [
#         "a piece of furniture",
#         "list of facts & figures"
#     ],
#     "cat": "a small animal",
# }
# print(dictionary)


# wap to enter marks of 3 students from the user and store them in a dictionary


# dictionary = {}
# for i in range(3):
#     subject = input("Enter subject name: ")
#     marks = input("Enter subject marks: ")
#     dictionary[subject] = marks
# print(dictionary)


# store 9 and 9.0 in set (string form, tuple form)
# values = {9, "9.0"}
values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)

# ok