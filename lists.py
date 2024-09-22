#LISTS

#List is a sequence of elments. They are defined as []

my_list = []

#Converting other types into list

#Strings
my_name = "Brian"
print(list(my_name)) # list(string) converts string into a list

sentence = "my name is Brian"
split_sentence = sentence.split() # converts a string into a list
print(split_sentence)

# split can divide strings through a character

my_email = "brianosora123@gmail.com"
split_email = my_email.split('@')
print(split_email)

# convert range to a list

new_range = list(range(1, 20, 3)) # list(range(start, end, step_size)) converts a range into a list
print(new_range)

#joining a list
my_name = ["My", "name", "is", "Brian"]
answer = '-'.join(my_name) # 'joiner'.join(list_name) method is to join elements of a list.
print(answer)

#Unpacking a list
point_x = [0,2]
point_y = [1,3]
x1, x2 = point_x
y1, y2 = point_y
print(x1, x2)
print(y1, y2)

#LIST OPERATORS

# + operator is used to concatenate lists
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a + b
print(c)

# * operator is used to multiply elements of a list
d = ["Brian", "Osora"]
e = 4 * d
print(e)

#Accessing items in a list through indexing

a_list = [1,2,3,4,5]

a_list[0] #returns the first item in a list
a_list[-1] #return the last item in a list
a_list[1::2] #return the elements in a list
a_list[::2] #return the elements in even position in a list
a_list[::] #creates a copy of the list
a_list[::-1] #reverses a list

# updating a list through index
a_list[0] = 6
a_list[-1] = 9

#list methods

test = [1,2,3, 'Mercedes', 5,8,9, 'Benz']

#append(element) adds element in the last position in list
test.append('Range rover')
print(test)

#insert(index, element) inserts element in specified position
test.insert(1, "Brian")
print(test)

#extend(new_list) is used to concat a list into another list
new_list = [['Silicon Valley', 'Hollywood', 'Vegas']]
test.extend(new_list)
print(test)

#sorted(list) sorts a list creating a new list
letters = ['d', 'z', 'a', 'b', 'm', 'g']
sorted_letters = sorted(letters, reverse = False) #reverse dictates the order of sorting True - descending, False - ascending
print(sorted_letters)

#.sort() sorts a list altering the original list
letters.sort(reverse = True)
print(letters)

#.pop(index) removes element from a list and returns the element
cars = ['Mercedes', 'Range', 'Porsche', 'Tesla', 'BMW', 'Toyota']
deleted_car = cars.pop(4)
print(deleted_car)

#pop() without index automatiocally removes only the last element in list
deleted_car = cars.pop()
print(deleted_car)

#del list[index] deletes item from list in index position and return none
del cars[0]
print(cars)

#remove(element) removes element from list
cars.remove('Porsche')
print(cars)

#Looping through a list using for loop

names = ['Brian', 'Emma', 'Mark']

for name in names:
	print(name)



