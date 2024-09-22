#string is a sequence of characters
name = "brian osora"
print(name.title()) #title converts str to title case each word starts with capital letters
print(name.upper()) #converts entire string to capital letters
print(name.lower()) #convert entire dtring to small leters
print(name.capitalize())#converts the first letter of string into capital letter like in a sentence

message = "The creator of 'Python' is called Monty Python."
print(message) #You can use both double and single quotes in python

first_name = "Brian"
last_name = "Osora"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!") #using variables in strings using f-strings
print("Hello, {0} {1}".format(first_name, last_name))

print("\tpython") #\t adds tab space to a string
print("Hello\npython") #\n adds new line

programming_languages = "Languages:\n\tPython\n\tJava\n\tJavaScript\n\tC++" #you can use both \n and \t together.
print(programming_languages)

#removing whitespaces or characters at the end
#inside the strip function we can add characters that can be removed such as "#"
favourite_language = " python "
favourite_language = favourite_language.rstrip() #removes whitespaces to the right
favourite_language = favourite_language.lstrip() #removes whitespaces to the left
favourite_language = favourite_language.strip()  #removes whitespaces both on left and right
#strip() function works temporarily you should assign it to its original variable after applying the method to save the changes.

#You can add and multiply strings together
my_name = first_name + last_name # Adding strings together is also known as concatenation
print(my_name)

repeat_name = 4 * "Osora"
print(repeat_name)

#String Operations

#find the length of a string
sentence = "Welcome to my learning."
print(len(sentence)) # len() is used to find the length of a string.

#find the index of a character in string
print(sentence.index("o")) #it returns the position of the first occurence of the character in the string.
print(sentence.count("W")) #counts the number of characters in string.
#find() looks for character insidde the string if it does not find it will return -1. you can specify the position you can start searching for and where you canend the search.
print(sentence.find("e", 3, 6)) 
print(sentence.find("x"))
print(sentence[3]) #prints the character at index 3

#slicing strings
#normal index

print(sentence[3:7])#prints characters from index 3 to 6
print(sentence[3:])#prints characters from index 3 to the end
print(sentence[:7])#prints characters from beginning to index 6
print(sentence[3:7:2])#prints characters from beginning to index skipping by 2 [start, stop, step]
print(sentence[::])#copies the entire string
print(sentence[::-1])#reverses the string

#negative index
#string[end, start, step]
print(sentence[-1]) #prints the last character in the string.
print(sentence[:-1]) #prints all characters except the final character in a string
print(sentence[-10:-2]) #prints all charactes between -7 and -2 position.

#string functions
greeting = "Hey Brian"
print(greeting.split(' '))
print(greeting.split()) #these two split strings into a list.
#you can add characters in the split function that can be used to split such as '@' to split emails

print(greeting.startswith("Hey"))
print(greeting.endswith('Osora')) #prints true or false

#Exercise
personal_message = "Hi, Brian. Would you like to study some python today?"

my_name = "briAn Osora"
lower_case_name = my_name.lower()
upper_case_name = my_name.upper()
title_case_name = my_name.title()

print(lower_case_name)
print(upper_case_name)
print(title_case_name)

famous_person = "Albert Enstein"
quote = F'{famous_person} once said "A person who never made a mistake never tried anything new."'
print(quote)

first_name = "\tBrian"
second_name = "\n\tOsora"
person_name = first_name + second_name
print(person_name)

first_name = first_name.lstrip()
second_name = second_name.lstrip()
person_name = first_name + second_name
print(person_name)

#replace
text = "Hello there Brian"
print(text.replace('there', 'Captain'))

# in operator
#checks if a character is in a string
print('Captain' in text)

#STRING COMPARISON
# python uses ASCII American Standard Code for Information Interchange for comparison
print('a' > 'A') #The ASCII code for 'a' is greater than 'A'.
print('orange' > 'banana')
print(ord('A'))
print(ord('a')) #ord function is used to check the ASCII Code for characters.
print(ord('o'))
print(ord('b'))



