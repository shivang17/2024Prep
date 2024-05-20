# Key-value pair

dict1 = {
    "x" : 1,
    "y": 2
}
print("dict1", dict1)
# You can create a dictionary using the dict in-built function

dict2 = dict(x=1,y=2)
print("Using dict function", dict2)
# Similar to list, the values can be accessed but not similar to list since the keys are not indexed but have the string. So, dict1["x"] will return 1.

# We can modify the value of individual key by assignment operator. 

dict2["x"] = "Changed"
print("Dict 2 after changing: ", dict2)

# You can also add a key value pair with assignment. 

dict2["z"] = 30
print("Dict 2 after adding using assignment", dict2)

# Invalid key will fetch an error. Check if the key exists before accessing
if "a" in dict2:
    print("Present")

# Second method: Use get method, it will return "None" if the key does not exist. You can also determine what value you want to be returned if the key doesn't exist, by passing in a second argument as follows:
# dict2.get("a")

dict2.get("a",0) 
# Delete item

del dict2["x"]
print("Item deleted", dict2)

# Iterate over a dictionary or the items of the dictionary. Let me show you what I mean:

for x in dict2: # This will only fetch the key
    print(x)

for key, value in dict2.items():
    print("Unpacking:  ", key, value)


# To understand dictionary comprehension, let's go back to list comprehension:

# Let's say we have:

values = []
for x in range(5):
    values.append(x *2)
# the above can be replaced by list comprehension as:

values_1 = [x * 2 for x in range (5)]
print(values_1)

# We can also use the above kind of comprehension with set and dictionaries too.

values_for_set= {x *2 for x in range (5)}
print("Set comprehension: ", values_for_set, type(values_for_set))
# The above will generate a set. The fundamental difference between set and dictionary is that dictionary will have key value pairs. 

# So, the comprehension can be used to generate the dictionary in the following ways

values_for_dict = {x : x *2 for x in range(5)}
print("Dict comprehension: ", values_for_dict)

# If you use the () brackets for tuple comprehension, it will return a generator object instead, which will be discussed in the generator.py file