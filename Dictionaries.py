#Dictionaries
#dictionary is a sequence of key value pairs
# Deining a dictionary

a_dict = {}
b_dict = dict()
car = {
	'make': "Mercedes Benz",
	'model': 'E250',
	'Year': 2025
}

#access items in a dictionary
print(car['make']) #dict_name[key]

#Add elements into a dictionary
car['owner'] = 'Brian Osora' #this can also be used to reassign a key in dictionary
print(car)

car.update({'model': 'G63'}) #update(dictionary) adds key-value into a dictionary or updates
print(car)

#Delete elements from a dictionary
#We use pop(key) and del to delete

year = car.pop('Year') #pop(key) return the deleted value
print(car)
print(year)

del car['make'] #del return None
print(car)

#Create a copy of a dictionary
new_car = car.copy()
print(new_car)

#Read elements of a dictionary
dict_items = car.items()
print(dict_items) #returns a list of tuples of keys and values of dictionaries

dict_keys = car.keys()
print(dict_keys) #returns a list containing keys of the dictionary

dict_values = car.values()
print(dict_values) #returns a list containing values of a dictionary

answer = car.get('make', 0)
print(answer) #get(key, false_value) the function gets the value of the key in dictionary if it is not available it returns the false valuable

answer = car.get('owner', 0)
print(answer)

#Looping a dictionary
for x in car: #this will automatically loop over the keys and return the keys
	print(x)

for key, value in car.items():
	print(key, value) #this prints the keys and values of the dictionary

for key in car.keys():
	print(key) #returns the keys of the dictionary

for value in car.values():
	print(value) #returns the values in the dictionary

#loop over multiple dictionaries
for x in (a_dict, b_dict, car):
	print(x)