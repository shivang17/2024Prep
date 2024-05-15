# Lists, Tuples, sets, and dictionaries are the building blocks of the
letters = ["A", "B", "C"]
list_of_letters = [list(letters)]
print("List of letters:", list_of_letters)
numbers = [1, 2, 3]
merged = [letters, numbers]

print(merged[0])
print(letters == merged[0])  # True

# If you want to create a list of numbers with same value of a very large number. Let's see how it can be done
zeros = [0] * 5
print(zeros)  # [0,0,0,0,0]

combined = zeros + letters
print(combined)

# Understanding list() function. It takes in an iterable and returns the list. Let's understand with an example
list_of_numbers = list(range(10))
print(list_of_numbers)

# If you pass a string, it will convert into a list with individual characters as the elements of the list

# Accessing items in a list
# [0], [0:3] [:3], [2:]

# Two ways to sort a list

# list_name.sort(), list_name.sort(reverse=True), the reverse parameter sorts the list in descending order.
# You can also add the third parameter, which will be a numeric value.
print(list(range(20)))

# Unpacking a list:
# [first, second, third, fourth] = [1, 2, 3, 4]
# print(first) OR

first, second, third = [1, 2, 3]
print("First: ", first)
# Unpacking rule: The number of items in the list should be same as the number of variables you assign. If you want to create an exception, you should use *. Let's understand:

first, *random, last = [1, 2, 3, 4]
print("What is the value of random?", random, type(random))


# Looping over list:
for letter in letters:
    print(letter)
# To get the index of each item, we have enumerate function
# So,

for letter1 in enumerate(letters):
    print(letter1)

print(enumerate(letters))

# Add elements at the end of list.
letters.append("4")

# When function is part of an object, it is called method
print(letters)
# Adding the element at any given point in the list

letters.insert(4, "Fifth")
print(letters)
print("What is a letter", letter)

# Pop and remove

list_2 = [1, 2, 3, 4, 5]
list_2.pop()
# pop removed it from the end, but you can also pass an index.
print("List 2 pop:", list_2)

list_2.pop(1)
print("List 2 removed the value from index 1?", list_2)

# If you do not know the index, you should just use remove function instead of pop and pass in the exact value you would like to remove


list_2.append("Shivang")
list_2.remove("Shivang")
print("Remove function used: ", list_2)


# del statement, the range is accepted by del.
# To remove all elements, use clear method

list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

del list_3[0:3]

print("Del statement used on list_3", list_3)
list_3.clear()
print("Entire list deleted?", list_3)

# Finding index:

list_4 = ["Shivang", "Suchak", "Piano", "Software", "Inc"]
print(list_4.index("Shivang"))

# If you try to call index which doesn't exist here, it will throw an error. Other languages generally return -1, but Python is different in this case.
# In order to prevent this, check the value first using if conditions before reading the index of it.

# So,

if "Sanjna" in list_4:
    print(list_4.index("Shiv"))
else:
    print("Couldn't find Shiv")
    print(list_4.index("Suchak"))

# Another important method would be count. If the count returns 0 then it means the element is not present in that array.
print(list_2.count("d"))


# Let's understand sorting again.

numbers_to_sort = [18, 12, 13, 27, 7, 5,]
numbers_to_sort.sort()
print(numbers_to_sort)

# To sort the order, we can pass a parameter named `reversed=True`

numbers_to_sort.sort(reverse=True)
print(numbers_to_sort)

# Another way is a buil-in function, "sorted"

sorted(numbers_to_sort) 
# sorted will return a new sorted list
print(numbers_to_sort)

use_sorted_method = [49,34,42,22,18,5,92]
print(sorted(use_sorted_method))
print("remains unchanged: ", use_sorted_method)
# Similar to sort method, the sorted function can also take the second parameter as reverse=True/False

# What if we have the tuples which we want to sort

# Imagine we are building app for processing orders. We have list of items as tuple
items = [
    ("Product 1", 10),
    ("Product 2", 32),
    ("Product 3", 23)
]

# Let's try to use sort method, similar to what we tried for strings and numbers

items.sort()
print("Items sorted: ", items, end="\n")
# Nothing changes because Python doesn't know what to sort the list

# Define a function to sort

def sort_item(item):
    return item[1]

# items.sort(sort_item)
#Just passing the reference of the function and not calling the function. This should ideally be trying to sort whatever is returned from sort_item function.

# But this will throw an error, "sort doesn't accept positional arguments". So, only keyword arguments.

# key = sort_item

items.sort(key=sort_item)
print(items)

# Lamda function -> Anonymous function that we can pass it to a function as a parameter

# items.sort(key=lamda, item :items[1]) (arr.sort(key=lambda, item:expression)) , we don't need def and return

# Let's use more of lamba functions. We have list of items containing tuples. We want to transform the list into something else. 

list_of_items = [
    ("Product1", 9),
    ("Product2", 12),
    ("Product3", 15)
    
    ]
# We want to transform the above list of tuples into just the list of numbers. 

# Traditionally, here's how you will do it. 

# prices = []

# for item in list_of_items:
    # prices.append(item[1])

# print(prices) #Here, we have basically mapped the list of items into another list of prices. The better way to achieve this is through map function. 

# Map accepts two parameters, first is a function (we will pass in lambda function) and second is a iterable (list)

# Map function will apply lambda function on each item in the list
map(lambda item: list_of_items[1],list_of_items) 
#Lambda is a function that will convert each item into list. So, (lamda parameter: return item, the list) 

# The above will return a map object which is iterable.
# list(map(lambda item: list_of_items[1]))

price = list(map(lambda item: item[1], list_of_items))
print(price)

# Filter function

price_with_condition = list(filter(lambda item: item[1]>=10, list_of_items))
print(price_with_condition)

# List comprehension, similar to map and filter (Map and filter tend to be used by developers coming from functional programming language like JavaScript)

price_with_list_comprehension = [item[1] for item in list_of_items]
print("List comprehension: ", price_with_list_comprehension)

filtered_price = [item for item in list_of_items if item[1]>=10]
print("Filtered price: ", filtered_price)

# Zip function
list_5 = [1,2,3]
list_6 = [10,20,30]

# You would like to combine two lists as a list of tuple, such that the first element of the list 1 and first element of list 2 is one tuple and so on. This can be achieved through the built-in zip method

print("Zip function: ", list(zip(list_5,list_6)))
# Interesting thing is that zip accepts one or more iterables. So, we can also pass a string and it will spread across the other tuples. 

print("Zip with string: ", list(zip("abc",list_5,list_6)))