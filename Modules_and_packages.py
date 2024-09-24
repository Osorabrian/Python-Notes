#Module is a python file ending in .py
#Package is a special folder that has modules
#modules and packages are usually 
#import module_name as name
#to use the module we write module_name.method()

import math_operations #we have created a math_operations module and imported it

print(math_operations.add(2,3)) #we call the methods in the module
print(math_operations.subtraction(3,9))

import math_operations as mo

print(mo.product(4,5))
print(mo.division(6,3))

from math_operations import * #from the module name it imports everything not recommended
print(product(9,4)) 