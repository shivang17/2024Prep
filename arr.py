# In most of the cases of sequence of data that you want to iterate over, you will use list, but there is a similar data structure called array, which needs to be imported from a moddule. 

# The major difference between list and array is that, arrays have a fixed type, determined at the time of creating an array. 
# Arrays are only recommended to used when you encounter large sequence of number and you encounter any performance issues. 

# For all other cases, use lists and tuples by default

from array import array

list1 = [1,2,3]
arr = array("i",[1,2,3])
arr.append(4)
print("New array", arr)
# All similar methods are available in the arr