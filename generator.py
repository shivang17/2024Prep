from sys import getsizeof
# Consider a list of numbers, generated using list comprehension:

values = [x * 2 for x in range(10)]
# for a in values:
    # print(a)

print("Size of list: ",getsizeof(values) )

# This kind of generating list of numbers is good only if the number is small. Imagine the range was 1 million instead of 10, the above is not a great idea to generate. We can use generator in this scenario. 


# Generator object do not store in memory but generates a new value with each iteration. Let's see how it works.

values = (x *2 for x in range(10))

# for b in values:
    # print(b)

print("Size of generator object: ", getsizeof(values))

# The value decreases a lot for tuples, if the input is very high. 

check_list = [x* 2 for x in range (10000)]

print("List size: ", getsizeof(check_list))

check_tuple = (x*2 for x in range(10000))
print("Tuple size: ", getsizeof(check_tuple))

# Be aware that because generator objects don't store all items in memory, you won't be able to get the total number of items you're working with (i.e, it doesn't have the len object), because it generates during iteration and the length cannot be known ahead of time. 

# Unpacking operator: (Similar to spread operator in JS)

# If you have multiple items in a list and want to print individual ones , you can pass the unpacking operator (*)
numbers = [1,2,3]
print(*numbers)

# Another useful application of the above operator is when creating a list

# We generally use range function to create a list.
print(range(5)) # It gives back an iterable
# Unpack it using the * operator
print(*range(5)) # 0 1 2 3 4

values = [*range(5), *"Hello"]
print(values)

# You can have two lists, unpack the values in first and second and combine them. 

first = [1,2,3]
second = [4,5,6]

combined = [*first, *second] #Unpacked the values and put in one array
print("Combined: ", combined)
combined_without_unpacking = [first, second] 
print("Without unpacking: ", combined_without_unpacking)

# Unpacking dictionaries. 

dict1 = {"x": 1, "y": 2}
dict2 = {"x": 3}

dict_unpacking = {**dict1, **dict2, "z": "Unpacking addition"}
print(dict_unpacking) # In this scenario, the last value of x will be assigned