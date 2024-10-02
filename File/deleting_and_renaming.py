"""
We use os model
to delete we use remove() or unlink() method
to rename we use rename()
"""

import os

# os.rename('file_to_delete.txt', 'file_to_rename.txt') #rename(file to be renamed, new file name)
# os.remove('file_to_rename.txt') #deletes file
# os.unlink('file_to_delete_2.txt') #deletes file

#create file
with open('new_file.txt', mode = 'x') as file:
    file.write("This is a new file")

