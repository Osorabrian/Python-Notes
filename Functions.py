 #Functions are a block of statements that perform a certain task

#defining a function
def function_name():
	print("Hello World!")

#calling a function
function_name()

#functions take in arguments
def greetings(name):
	print("Hello, {0}".format(name))

#function calls pass parameters
greetings('Brian')

#DOCSTRINGS are strings in a function that describes what functions do
def car(make, model, year):

	"""
		Function tells you information about a car.
		parameters: car make, model, year of manufacturing.
		return: String
	"""

	car_info = "This is a {0} {1} {2}.".format(year, make, model)

	return car_info

print(car('Mercedes Benz', 'E350', '2015'))

#get information about the function
help(car)

#getting information about method through dunder attributes
print(car.__doc__) #gives docstrings of the method
print(car.__name__)#gives the name of the method
print(car.__module__)#gives the module of the method

#VARIABLE SCOPES

#function scope
def sum(a, b):
	addition = a + b
	return addition


# print(addition) will create an error because the variable's scope is in the function

#global scope
speed = 80

def calculate_speed():
	speed = 20
	return speed

# AS you can see you can access the variable in a function or any place in your code and it can only change in the function and not the global variable
print(calculate_speed())
print(speed)

#to change the global variable in a function we use global

def new_speed():
	global speed
	speed = 120
	return speed

#we first call the function that changes the global variable
new_speed()
print(speed) # the global variable has now changed.

#NAMED VARIABLES

#we can assign some arguments during defining of functions
def full_name(middle_name, first_name = "Brian", last_name="Osora"): #unassigned variables usually are at the left or starting end.
	return "{0} {1} {2}".format(first_name, middle_name, last_name)

print(full_name(middle_name = 'Isaboke')) #we only pass the unassigned argument as a parameter
print(full_name(first_name = "Emma", last_name="Nyabonyi", middle_name='Isaboke')) # you can change the values by assigning new values order does not matter.

