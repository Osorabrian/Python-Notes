#Tuple is a sequence of elements and is immutable

#creating a tuple
a_tuple = tuple()
b_tuple = (1,2,3,4)
c_tuple = ('a',) #creating a tuple with one element
t = 'a', 'b', 'c', 'x', 'y', 'z'
print(t)
name ="Brian"
print(tuple(name))

#We use indexing to access items in a tuple
#We can use slicing in tuples

#TUPLE COMPARISON
print(("a","b") < ("b", "a"))

print("abcd" > "abce")

print("No" < 'no')
#in comparison we start from left to right if one is greate than the other the comparison stops there

#TUPLE ASSIGNMENT
a = 20
b = 50

a,b = b, a
print("a:", a)
print("b:", b)


point_x = [10, 20]
point_y = [50, 60]

x1, x2 = point_x
y1, y2 = point_y

print(x1, x2)
print(y1, y2)

#TUPLES IN FUNCTIONS()

def sum_and_multiplication(n):
	summation= 0
	multiplication = 1

	for i in n:
		summation += i
		multiplication *= i

	return summation, multiplication

print(sum_and_multiplication([1,2,3,4,5,6,7]))

#divmod(dividend, divisor) returns a tuple (quotient, remainder)
answer = divmod(23, 4)
print(answer)

#zip() function in tuples
a = 'Brian'
b = [1,2,3,4]
answer = zip(a,b)
print(list(answer))

#when zipping two sequence of different lengths it will only zip the shortest length lets say one with length of 5 and another 8. It will return a list of tuples of 5

#Tuples and dictionaries

#convert tuple into dictionary
# a_tuple = (1, 2, "Brown", 5, ['c', 'd', 'e'])
# dict_tuple = dict(a_tuple)
# print(dict_tuple)

#Sorting tuples
#USING KEY attrinute in sorting helps us ioentify the variable that determines how we sort
numbers = (1,6,99,4,2,7,8)
new_numbers = sorted(numbers, key = lambda x: x, reverse = True) #we sort based on the numbers
print(new_numbers)

n_tuple = [("a", 34), ("b", 12), ("c", 9), ("d", 20)]
n_tuple.sort(key = lambda x: x[1]) #in this case we are sorting the list based on last item in each tuple
print(n_tuple)

n_tuple.sort(key = lambda x: x[0]) #in this case we are sorting the lisst basedon first element of each tuple
print(n_tuple)


