"""
To search for files or folders we use string methods such as startswith(), endswith(), find()
fnmatch module
"""
from pathlib import Path
import fnmatch

search_path = r'/Users/user/Desktop/Python/File'

files = Path(search_path)
for file in files.iterdir():
    #checks if it is_file() 
    if file.is_file() and file.name.endswith('.py'):
        print(file.name)
        
pattern = "*.txt"

for file in files.iterdir():
    #checks if file is a folder or directory
    if file.is_dir():
        print(file.name)
        
for file in files.iterdir():
    if file.is_file() and fnmatch.fnmatch(file.name, pattern):
        print(file.name)