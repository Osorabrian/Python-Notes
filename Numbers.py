#Numbers in python
import math
#integers, float and complex are data types in python

#operations
print(3+2) #addition
print(3-2) #subtraction
print(3*2) #multiplication
print(3**2)#exponential
print(3/2) #division always returs a float
print(3%2) #modulus return only the remainder
print(3//2)#floor division returns only the whole number
number = 14_000_000_000 #underscores can be used to seperate numbers for easy reading but has no effect
print(number)

#multiple assignments
x,y,z = 1,2,3
print(x)
print(y)
print(z)

#constants
MAX_NUMBER = 500
print(MAX_NUMBER)

#try it exercise
favourite_number = 1
print(f"my favourite number is {favourite_number}")

help(math) #this givs your more information regarding the module

answer = math.sqrt(16) #calculate square root
print(answer)

answer = math.cbrt(8) #calculate cube root
print(answer)

print(math.pow(3,2))#exponentiate 3 by 2
