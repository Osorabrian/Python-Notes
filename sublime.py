#Comprehension is an easy way to loop over a sequence.

#list comprehension

#prints a list of even numbers between 0 and 10
a_list = [number for number in range(11) if number % 2 == 0]
print(a_list)

#loop over nested list
b_list = [[1,2,3,4], [5,6,7,8], [9,10,11,12,13], [14,15,16,17,18]]
odd_list = [element for i in b_list for element in i if element % 2 != 0]
print(odd_list)

names = ['Brian', 'Mark', 'Emma']
numbers = [1,2,3]
rank = list(zip(names, numbers))
print(rank)

#set comprehension 

#returns a set of letters in name without the space
full_name = "Brian Osora"
a_set = {letter for letter in full_name if letter != ' '}
print(a_set)


#dictionary comprehension

#prints index of each letter as its key
count_dictionary = {key: value for key, value in enumerate(full_name)}
print(count_dictionary)
