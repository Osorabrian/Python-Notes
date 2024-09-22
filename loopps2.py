# Python has two loops while loop and For loop

#WHILE LOOPS

i = 0
n = 10

while i <= n: #the first statement is a condition statement. if statement is true it executes the statement below it.
	# print(n)
	n -= 1 #condition variable if not set the loop will be an infinite loop

# FOR LOOPS
# loops over a sequence like strings, lists, range

# for i in 'Brian':
# 	print(i)

#range(start, end, step)
for i in range(10, 1, -1): #print numbers backwardsd from 10 to 1
	print(i)

#while looping over a sequence we might need its index we will use the enumerate()method
for index, letter in enumerate('python'):
	print(index, letter)

#nested loops
name = 'Brian Osora'
# for i in name.split():
# 	for n in i:
# 		print(n)

# continue statement skips to the next iteration
for char in name:
	if char == ' ':
		continue 
	else:
		print(char)

#break statement is used to exit a loop.
count = 0
name = "Hello, My name is Brian"

for x in name:
	count += 1
	if x == 'y':
		break

print("The position of y is: ", count)

#for..else statement is uses to check if your loop has susccessfully completed without breaking.

for n in name:
	if n == 'y':
		print("found y")
		break
else:
	print("loop succesfully completed")


for letter in name:
	if letter == 'x':
		print("found x")
		break
else:
	print("loop has not found x")