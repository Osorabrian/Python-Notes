#Exception handling is the process of managinf errors

#Raise used to raise an error

user_input = "Brian2" #input("Please enter a name: ")

for letter in user_input:
	if not letter.isalpha():
		raise Exception("Please enter a valid name")
	print(letter)

#Assert. Assertion makes sure the code stops if it does not assert to true

for letter in user_input:
	assert letter.isalpha(), ValueError("Please enter a valid name") # or Exception("Please enter a value") or "Please enter a value"
	print(letter)

#Try...except it executes code in the try block if it fails it executes the except.

try: #it trries to execute the code in the try block
	for letter in user_input:
		assert letter.isalpha()
		print(letter)
except: #excutes the block of code if 
	print("Please enter a valid name")

#check if the element at the index is available if not returns index error
my_list = [1,2,3,4,5]

try:
	assert my_list[9]
except IndexError as ie:
	print(ie)

#try..except...else. this executes try if there is no error it continues to else block

try: #python tries to execute this block of code
	file = open("python.txt")
except FileNotFoundError as fe: #if there is an error it executes this block of code
	print(fe)
else: #if the it succeds trying to execute it execute this block of code
	file.read()
finally: #whether it passes or fails it executes this block of code
	try: #tries to close file if it is available
		file.close()
	except: #if it fails to close the file it executes this code
		print("File has been closed")

#pass when you dont want to return an error
def list_sum(arr):
	answer = 0
	for number in arr:
		try:
			assert int(number)
		except:
			pass
		else:
			answer+=number

	return answer

print(list_sum([1,2,3,'g',7,8,'z']))

