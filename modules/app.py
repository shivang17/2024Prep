# The shortcut to import all modules is to use *,but you may end up importing a lot of unncessary objects, function, etc. Also, some of the objects with same name might override it.

# Another way to import the module is through just using import <moduleName>

"""
__pycache__ -> It is for faster loading of the compiled version of the file. The way it determines if the code is up to date is by comparing the timestamp of the source file and pycache, if it is different, pycache will re-run the file and store it. 
"""

import ecommerce.sales
import sys
# print(sys.path) #When we use import <moduleName>, Python search for it in all the path that sys.path returned. As soon as it finds, the search stops. 

"""From a sub directory -> If you import as sales, it will not allow, hence it's import modules.ecommerce.sales"""


"""Another method will be to create an __init__.py file"""

"""ecommerce folder is like a package. Package is like a container for one or more modules. Package is mapped to a directory, a module is mapped to a file"""
"""Similar approach can be used for sub-packages"""


"""Absolute v/s relative import for intra-package references"""

"""main method: """

"""__init__ method folder will be treated as package (containing one or more modules)"""
print("App initialized", __name__)
