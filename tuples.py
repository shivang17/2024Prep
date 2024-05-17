# Tuple is a read-only list

# It can contain sequence of objects, but cannot modify the sequence. 
# Tuple can be also defined without the paranthesis. 

point = (1,2)
# Tuple can also be defined as point = 1,2 OR 1, (If you only use 1, it will be an integer). You can check by print(type (point))

# You can concatenate multiple tuples. 

point_two = (1,2) + (3,4)
print("Tuple concatenated: ", point_two)

# You can also multiply the two tuples. 

point_multiply =  (1,2) * 3
print("Tuples multiplied: ",point_multiply)

# You can convert list to tuples. 

list_to_tuple = tuple(["Shivang", "Suchak"])
print("List to Tuple: ", list_to_tuple)
# If you pass in just the string, it will separate each value in the string to the tuple elements. For example, if you pass "Shivang Suchak" as a string to the tuple function, it would have returned ("S", "h", "i", ....)

# Similar to list, tuples' values are accessible by index. point[0], point[0:3]

# Unpacking of the tuple:

x,y = point
print("X:", x)
# Tuples are immutable. So, trying to assign/change the value will result in an error. 

# We may ask where in the real world will tuples be used? Let's say you are dealing with sequence of objects and you want to make sure that you don't accidentally modify the sequence. 

