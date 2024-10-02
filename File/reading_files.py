"""
    To read a file there are numerous ways to reading a file:
    read() -> all content or upto a certain point e.g read(2)
    readline() -> reads a single line and waits for the next one
    readlines() -> reads all the remaining lines
    for loop -> using a for loop to print all the lines
"""

#read

with open("words.txt", encoding = 'utf-8', mode = 'rt') as file: #rt means read as text
    everything = file.read() # it reads all context of file
    print(everything)
    
with open("words.txt", encoding="utf-8", mode = 'rt') as file:
    context = file.read(10) #this reads only the first three elements of the file
    print(context)
    
with open("python-logo-0.webp", mode = 'rb') as file: #rb means read as binary
    content = file.read()
    # print(content)
    
file = open("words.txt", encoding= 'utf-8', mode = 'rt')
print(file.readline()) #prints first line of a file
print(file.readlines()) #prints reamining strings as a list
file.close()

file = open("words.txt", mode='rt')
for sentence in file:
    one_by_one = sentence.strip() #removes spaces between lines or we can use split if lines has one word
    print(one_by_one)
    


    

    
