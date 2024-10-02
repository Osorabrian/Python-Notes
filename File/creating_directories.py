"""
we use os module and pathlib library to create directories
mkdir() -> to make a single directory
mkdirs() -> to make many directories
"""
import os
from pathlib import Path

#crete directory
# os.mkdir('exaple_1_directory')

#create directory using pathlib library
# p = Path('example_2_directory')
# p.mkdir()

#create multiple directories
# os.makedirs('folder_1/folder_2/folder_3', exist_ok=True) #creates sub folders

#create multiple directories using pathlib library
p2 = Path("folder1/folder2/folder3")
p2.mkdir(parents=True)
