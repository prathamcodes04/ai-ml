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


'''
Attributes - variable name or data
- class.attr
- obj.attr
- object attr > class attr
- data which different for every value we use self.name, self.class, self.roll
'''

# class Student:
#     college_name = "surajmal"
#     name = "anonymous" #class attr
#     def __init__(self, name, marks): 
#         self.name = name #obj attr > class attr
#         self.marks = marks
#         print("adding new student in db...")

# s1 = Student("karan", 97) 
# print(s1.name)  



'''
Methods are functions that belong to objects
- class is a collection of attributes (properties) and methods (functions)
-
'''

# class Student:
#     college_name = "surajmal"
#     name = "anonymous" #class attr
    
#     def __init__(self, name, marks): #constructor
#         self.name = name #obj attr > class attr
#         self.marks = marks
        
#     def welcome(self): #method 1
#         print("welcome student", self.name)
    
#     def get_marks(self): #method 2
#         return self.marks

# s1 = Student("karan", 97) 
# s1.welcome() #calling method
# print(s1.get_marks())



# practice
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:", sum / 3)
        
# s1 = Student("tony", [99, 98, 97])
# s1.get_avg()
        
# # we can change attribute value too
# s1.name = "ironman"
# s1.get_avg()




'''
Static methods dont use self parameters (work at class level)
- uses decorator: allows use to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
- @staticmethod: converts a normal function into static function
'''

# class Student:
#     @staticmethod #decorator
#     def college():
#         print("ok sorted")
# s1 = Student()
# s1.college()



'''
Four pillars of oops: abstraction, encapuslation, inheritance and polymorphism

- abstraction: hiding the implementation details of a class and only showing the essential features to the user

- encapsulation: wrapping data and functions into a single unit (object)

- Inheritance: 

- Polymorphism: 
'''


# abstraction
class Car 
 