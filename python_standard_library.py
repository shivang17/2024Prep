"""
Python has batteries included philosophy which means it comes with a comprehensive library of packages and modules that provide common feature which are required when building real world applications. 

We will be working on following standard libraries:

1. Files and directories
2. SQLite Database
3. Date Time objects
4. Random values
5. Send emails and so on


"""

"""Working with path file"""

# Let's import the Path class from the module

from pathlib import Path

# There are multiple ways to create a path, absolute and relative.
Path("C:\\Program\\...")

Path("/usr/local/bin")
# Current folder path creation
Path()
# Relative path:

Path("/ecommerce/__init__.py")

# Combine paths together

Path() / Path("/ecommerce")

# Combine with a string

Path() / "ecommerce" / "__init__.py"
# Home directory
Path.home()

path = Path("/ecommerce/__init__.py")
path.exists()
path.is_file()
print(path.name)
print(path.suffix)
print(path.stem)
print(path.parent)

# Create a new path object, based on existing path, change the file name it's extension. 
# new path object

path = path.with_name("file.txt")
print("New file", path, path.absolute())

# with_suffix is a method used to change the extension of the file. path.with_suffix(".txt") // __init__.txt


# Working with Directories
path2 = Path("/ecommerce")
print(path2.exists())
path2.mkdir()
path2.iterdir() #returns Generator object, new values every item it's iterated, since we have millions of files sometimes to work with, within a directory. If the files aren't too long, you can use list comprehension instead of generator

for p in path2.iterdir():
    print(p) #generator

# List comprehension [p for p in path2.iterdir()]

"""
Working with files and zip files
"""