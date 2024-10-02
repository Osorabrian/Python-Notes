"""
Creating a zip folder we use shutil.make_archive(folder_name, "zip", new_folder_name)
"""
import shutil
import zipfile

#create zipfile
shutil.make_archive("folder_1", "zip", "folder_1")

#open zipfile
files = zipfile.ZipFile("folder_1.zip")
print(files.printdir())

files.extractall()

files.close()
#