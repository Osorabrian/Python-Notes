"""
File is a set of bytes that stores data.

File Types:
1) Text Files e.g html, txt, xml, java
2) Binary Files e.g pdf, doc, png

Encoding refers to how data is stored in a file.

 Common Encodings
 a) ASCII - American Standard Code for Information Interchange (128 Characters)
 b) Unicode
 
 modes:
 r - read
 w - write
 a - append
 x - create
 t - text file
 b - binary file
 + - update
"""

#opening a file
file = open("words.txt")
file.close()

#opening with encoding
file = open("words.txt", encoding="utf-8")
print(file.read())

#all files have to be closed to avoid memory leak
file.close()

#Opening using a context manager (With) automatically closes a file after opening it
with open("words.txt", encoding="utf-8") as file:
    context = file.read()
    print(context)
