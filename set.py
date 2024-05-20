# Set is an unordered collection of items. It contains unique values and are represented by {}

first = set([1,2,2,3,3,4])
print(first)

second = {1,5,5} #This will automatically filter the duplicated values
print(second)
# We have the methods available on set, similar to that of a list
# Sets are used for mostly mathematical operation, especial connected with the mathematical concept of set. 
# Union, Intersection, etc. 
print("Union: ", first | second) #Includes all items in first or second

print("Intersection", first & second) # Includes all items in both first and second
print("Difference", first - second) # {2,3,4} ({1,2,3,4} - {1,5})
print("Symmetic difference: ", first ^ second) #It will return items that are either in first or second, but not both
# Items are not in sequence. So, you cannot access it using index. (It will throw an error)
# You can check the existence. For example, if 1 in first: print("Yes")