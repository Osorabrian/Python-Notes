"""
In writing to files we have two modes:
w -> write is dangerous it clears the file and opens as ablank file
a -> append, appends the new content to the file
"""

with open("writing.txt", mode = 'w') as file:
    file.write('ddvdvdfvfdv\nerfergergreg\neererergrgregre')
    
with open("writing.txt", mode="r") as file:
    print(file.read())
    
with open("writing.txt", mode = 'a') as file:
    file.write("\nBrian Osora Isaboke")
    
with open("writing.txt", mode="r") as file:
    print(file.read())
    
with open("writing.txt",mode='a') as file:
    string_list = ['\nWe are here', '\nTo conquer the world', '\nAnd so be it']
    file.writelines(string_list)

with open("writing.txt", mode="r") as file:
    print(file.read())
    
