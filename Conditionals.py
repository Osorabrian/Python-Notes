# conditional statements are used to perform tasks based on true vs false

def conditionals():

	# USER INPUT
	user_input = input("Please enter a number: ") #input function prompts a user to enter a value

	# values inputted are all of string type  so we have to change into integer
	 # n  = int(user_input)

	 #we can also implement controls to ensure our code runs perfectly without errors
	if user_input.isdigit(): #checks if user input is a digit
		n = int(user_input)
	else: 
		print("Please input a number")
		return


	if n > 0: # if checks if statement is true or false. it only executes if statement is true
		return "Positive"
	elif n == 0: # else if performs extra statement checks if statement is true it executes if flase proceeds the next statement
		return "Zero"
	else: #if statement does not meet any conditions it will execute this statement
		return "Negative"


print(conditionals())

"""
	TIPS
	-You can use \ to seperate code if it is long into multiple lines
	
"""
