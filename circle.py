import math
#LAMBDA FUNCTIONS

power_of_x = lambda x: x **2
print(power_of_x(2))

area_of_rectangle = lambda x, y: x * y
print(area_of_rectangle(4, 5))

#Boolean functions

def is_integer(x):
	return x % 2 == 0

print(is_integer(6))

#Assign a function to another variable AKA Alising

def cube(n):
	return n**3

q = cube #assign a variable to this function
print(q(3))
print(cube(4))

#uknown arguments *args in cases where you may not know the actual number of parameters

def uknown_arguments(*args):
	return args

print(uknown_arguments([3,4,5,6], 'Brian'))

#functions retrurn functions

def multiply_by(n):
	return lambda a: a * n

multiple_of_2 = multiply_by(2)
answer = multiple_of_2(3)
print(answer)
