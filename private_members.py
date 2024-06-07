# We implemented the custom containers and magic methods in custom_containers.py file, but there's a problem here. 

# Let's try to understand what:

# For example: when the add method is used to add the tags in uppercase and then trying to access it by leveraging the get method, class gives access to the underlying dictionary, that is used to keep track of count of tags


# cloud = CloudTag()
# print(cloud.tags) will give empty dictionary and cloud ["PYTHON"] will return zero, but cloud.tags["PYTHON"] will throw a KeyError.

# To fix this, we need to hide the attribute from the outside, by using __ 

# The implementation is explained more in the custom_containers.py.
