"""
To delete a folder or directory we use os, shutil module and pathlib library
to delete we use os.rmdir(folder_name), or path.rmdir(folder_name) or shutil.rmtree(folder_name)
to move the folder we use shutil.move()
to copy files we use shutil.copy(src, dest)
"""

import os
import shutil
from pathlib import Path

#to delete

# os.rmdir("exaple_directory")

# folder_path = Path('example_2_directory')
# folder_path.rmdir()

# shutil.rmtree('folder1')

#to copy files
# path = os.getcwd()
# shutil.copy("/Users/user/Desktop/Python/File/delete_copy_move.py", "/Users/user/Desktop/Python/File/delete_copy_move_2.py")

# #to copy directory
# shutil.copytree("/Users/user/Desktop/Python/File", "/Users/user/Desktop/Python/File_2")

#to move folder or directory
shutil.move("/Users/user/Desktop/Python/File_2", "/Users/user/Downloads")


