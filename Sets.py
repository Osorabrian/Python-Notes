"""
SETS is a datatype that includes other data types.
Basic uses is membership testing and eliminating duplicate entries
They are unordered and unindexed.
Its elements are unique.
"""

#Create a set
a_set = set() #to create an empty set you have to use set()
b_set = set({1,2,3, 'a', 'b'})
c_set = {2,3,4,5}

#Convert other types into set

a_list = [1,2,3,4]
set_list = set(a_list) #convert list into a set
print(set_list)

name = "Brian"
set_name = set(name) #convert string into a set
print(set_name)

#Set methods

a = {'a','b','f','h','e','i','p'}
b = {'b','m','p','y','e','z','l'}
c = {'p','a','f'}


#INTERSECTION returns common items in both sets
answer = a.intersection(b)
print(answer)

#UNION return all elements in both sets
answer = a.union(b)
print(answer)

#DIFFERENCE retruns difference in two sets
answer = a.difference(b)
print(answer)

#ISDISJOINT checks if both sets are completely diferent
answer = a.isdisjoint(b)
print(answer)

#ISSUBSET checks if a set is a subset of another set
answer = c.issubset(a)
print(answer)

#ISSUPERSET checks if set is a superset of another set
answer = a.issuperset(b)
print(answer)

answer = a.issuperset(c)
print(answer)

#DIFFERENCE_UPDATE removes common differences
a.difference_update(b)
print(a)
print(b)

a = {'a','b','f','h','e','i','p'}
b = {'b','m','p','y','e','z','l'}

#SYMMETRIC_DIFFERENCE returns different elements of two sets
answer = a.symmetric_difference(b)
print(answer)

new_set = b.copy() #creates a copy of the set.
print(new_set)

b.clear() #removes all elements from a set
print(b)

sorted_set = sorted(new_set, reverse = True) #sort a set we cannot use sort() it is only for lists. returns a list.
print(sorted_set)

list_set = list(new_set) #convert set into a list
print(list_set)

new_set.add('A') #adds elements into a set
print(new_set)

new_set.remove('z') #removes elements from a set. if element is not found it will return an error.
print(new_set)

new_set.update({'x', 't', 'r'}) #update adds set of elements to a set
print(new_set)

answer = new_set.pop() #pop removes a random element from a set
print(answer)

new_set.discard('A') #removes certain element from a set. remove returns error if element not found discard method will not.
print(new_set)

