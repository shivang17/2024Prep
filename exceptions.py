# Checking things to make sure that mistakes are caught. 

# numbers = [1,2]
# print(numbers[3]) # This doesn't exist. So, it will throw an error (list index out of range)

try:
    age = int(input("Enter the age"))

except ValueError as ex:
    print("Wrong format, please try again...")
    print(ex)
    print(type(ex))

# You can also have else condition here which will be executed if you don't have an else condition here

print("Execution continues")

# Handling different exceptions

# try:
    # age_with_exceptions = int(input("Age: "))
    # xfactor = 10 / age_with_exceptions

# For a division, we should also include ZeroDivisionError:

try:
    age_with_exception = int(input("Enter your age: "))
    xfactor = 10 /age_with_exception

# You can add multiple exception in one line
except (ValueError, ZeroDivisionError) as e:
    # print(e)
    print("The operation isn't allowed")
# Once the python catches an exception caught by the try block, it will not go to catch the similar exception (ignore). 

# Finally is always excecuted. (Used to release external resources)

# Finally is used when we want the code to be executed irrespective of whether except block runs or it continues from try. For example, you open a file in the try block, but you will need to close it as it might be needed for some other services. 

# With statement:

# try:
#     with open("file.txt") as file: # You don't need to close the file when using the with, it automatically does it
#         print("File opened")
# except ValueError:
#     print("Value error:")

# How it works. file object (returned value from with), contains magic methods, enter and exit. When the object has enter and exit methods, it means the object supports the context management protocol(CMP). When the object has the CMP, we can use the "with" statement.

# You can open multiple files by just adding open clause after "as file: "

# Till now we have handled the excpetion, but we can also raise or throw an exception in the code. 
# Raising exception is costly and we need a better approach, let's talk about it. 

from timeit import timeit

code1 = """def calculate_xfactor(age):
    if age <=0:
        raise ValueError("Age cannot be zero or less")
    else: return 10/age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

print(timeit(code1, number=10000))

code2 = """def xfactor_timeit(age):
    if age <=0:
       return None
    else:
        return 10/age

xfactor_timeit = xfactor_timeit(-1)
if xfactor_timeit == "None":
   pass
"""

print(timeit(code2, number=10000))

# The difference is only visible and relevant when the number of times the function is going to run for a long time. 