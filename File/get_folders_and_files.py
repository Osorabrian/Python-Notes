"""
we use the os module 
using pathlib library
"""

import os
from pathlib import Path

#to get the path we use getcwd()
path = os.getcwd()
print(path)

#os.scandir() used to list the direct entries
result = os.scandir(path)
for file in result:
    print(file)
  
#os.listdir() returns a list of file
files_list = os.listdir(path)
for file in files_list:
    if os.path.isfile(file): #os.path.isfile(file_name) is used to check if the file name is a file.
        print(file)
    elif os.path.isdir(file): #os.path.isdir(file) checks if the file is a folder
        print(file)
        
#lists the directories for files
path_content = Path(path)
for file in path_content.iterdir():
    print(file)
    

    






