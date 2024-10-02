# OOP -> Object Oriented programming is the representation of real world objects
# Objects have attributes and methods.
# We use classes to create objects. Class is a blueprint for creating objects
# We use 'class' Keyword to create classes
#Classes have two operations attribute reference and instantiantion


class Car:
    
    invented = 1984 #class variable that all classes e.g car have
    
    #instance variable only belong to a individual object
    def __init__(self, make): #constructor method constructs the object. it takes paramentes and creates attributes
        self.make = make # self references to the current instance of object or class
        self.__price = 30_000 #private attributes are only accessed inside the class they have '__' in their attributes
        print("Car has been Created.")
    
    def body_type(self): #instance method
        return "SUV"
    
    def about(self):
        return f"This is a {self.make}"
    
    def sell(self):
        return f"The price of {self.make} is {self.__price}"
    
    def set_price(self, new_price): #setter method used to set attributes for private attributes
        self.__price = new_price
        
    def get_price(self): #getter methods used to get private attributes
        return self.__price

mercedes = Car('Mercedes Benz')

print(mercedes)

#To access the class variable by object
print(mercedes.invented)
print(mercedes.__class__.invented)

#To access the instance variable
print(mercedes.make)

#To call the object methods
print(mercedes.about())
print(mercedes.body_type())

#Private attributes
# print(mercedes.__price) #trtying to access the private attribute will raise an error AttributeError: 'Car' object has no attribute 'name'
print(mercedes.sell()) #You can access via methods

#INHERITANCE Classes inherit from other classes

class Truck(Car): #When inheriting from parent class we input the parent class in parentheses
    
    def __init__(self,make, payload):
        super().__init__(make) # we call the constructor of parent class
        self.payload = payload
        print("Truck is Created")
        
    def body_type(self): #ovverides method in parent class
        return "TRUCK"
    
    def capacity(self):
        return f"The payload of this truck is {self.payload}kgs."
        
actros = Truck('Actros',5000)
print(actros.body_type())
print(actros.payload)
print(actros.make)
print(actros.capacity())

#ENCAPSULATION (Information hiding)
"""
    Hiding inormation from other user and prevent from altering the attribute. We use private attributes.
    We use setter methods and get methods to set and access private variables.
    Encapsulation enables us to give all control to the class.
"""

#POLYMORPHISM It refers to the object taking different forms.

class Hatchback(Car):
    
    def __init__(self, make):
        super().__init__(make)
        print("hatchback has been created")

    def body_type(self):
        return 'HATCHBACK'
    
a180 = Hatchback()
print(a180.body_type())

def body_styles(car): #this function return different results based on the object as its parameter.
    return car.body_type()

print(body_styles(mercedes))
print(body_styles(actros))
print(body_styles(a180))
#as we can see the 