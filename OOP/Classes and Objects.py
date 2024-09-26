class Person:
    
    scientific_name = "human being"
    
    def description(self):
        return "A human is a living organism"
    
print(Person.scientific_name) #getting the class variable Class.variable

# print(Person.description()) # will return an error because it has no self parameter to fix this we have to:

male=Person()
print(Person.description(self = male))# we create an instance and then pass it to the method or
print(male.description())

#DELETING ATTRIBUTES AND INSTANCES
class Student:
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
std = Student('Brian', 23, 'A')
print(std.name)

#To delete attributes and instances we use del

#Deleting an attribute
# del std.name 
# print(std.name)

#Deleting an instance
# del std
# print(std)
