'''
OOPS (Object Oriented Programming)
- to map with real world scenarios, we started using objects in code
- in the beggining we use to do procedural or sequential programming
- then we learnt the concept of functions which taught us reusability increase and reduce redundancy
- procedural to functional programming, now we move to oop
- to reduce redundancy and increase reusability we use object and classes
-  we create class before object 
'''


'''
Class - is a blueprint for creating objects
'''

# creating class - multiple paramters can be added
# class Student:
#     name = "pratham gupta"

# # creating object (instance or instances of class)
# s1 = Student() #object
# print(s1.name)

# s2 = Student() #object
# print(s2.name)


# factory producing cars
# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)



'''
Constructor: is basically an __init__ function
- all classes have a function called __init__, which is always executed when the object is being executed.
- invoked during object creation
- Self parameter - is a reference to the current instance of the class, and is used to access variables that belongs to the class
- all the data being stored inside class or objects are called attributes
'''

# class Student:
#     #default constructors have only self
#     def __init__(self): 
#         pass
    
#     #paramterized constructors have paramters other than self
#     def __init__(self, name, marks): #self is the new object which s1 here as reference
#         self.name = name
#         self.marks = marks
#         print("adding new student in db...")

# s1 = Student("karan", 97) 
# print(s1.name, s1.marks)
# s2 = Student("arjun", 88) 
# print(s2.name, s2.marks)
