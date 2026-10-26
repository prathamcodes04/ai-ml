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
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True #these unecessary steps not showed
#         self.acc = True
#         print("car started...") #this showed

# car1 = Car()
# car1.start()

# practice
# create account class with 2 attributes - balance and account no.
# create methods for debit, credit and the balance

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
    
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Total balance =", self.get_balance())
          
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("Total balance =", self.get_balance())
          
#     def get_balance(self):
#         return self.balance
    

# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(10000)



# OOPS PART 2
'''
del keyword - used to delete object properties or object itself 
'''

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("pratham")
# print(s1.name)
# del s1
# print(s1)



'''
Private(like) attributes and methods
- these are ment to be used only within the class and are not accessbile from outside the class
- Public: method and attribute can be accessed outside class and Private: cant be accessed outside class
- to make any attribute private just add two underscores in front of it: __acc_pass
- this concept is applied conceptually in python, our attributes and functions are like private but not actually private
'''


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass #private class
    
#     def reset_pass(self):
#         print(self.__acc_pass) #works here as it is inside class

# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# # print(acc1.__acc_pass) #cant be accessed as it is outside class
# print(acc1.reset_pass()) 

class Person:
    __name = "anonymous"
    
    def __hello(self): #these functions.methods are made to being used by another function internally
        print("hello user")
    
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome()) #welcome calls hello inetrnally
# print(p1.__name)
# print(p1.__hello())