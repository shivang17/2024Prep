# Break down the code into reusable chunks

# Start with def followed by the name and underscore to separate multiple words:

def greet():
    print("Hi there")
    print("Welcome aboard")


greet()

# difference between parameter and argument is, parameters are passed in the function definition and arguments is something that is passed during function call. So, actual value of the parameter.


def greet_with_parameters(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


greet_with_parameters("Shivang", "Suchak")
# By default, all funciton parameters are mandatory. So, if you call the function greet_with_parameters("Shivang"), it will throw an error since the second argument is also mandatory.

# Two types of functions 1 - Perform a task (print on terminal), 2) Return a value (round function to calculate and return a value)


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Shivang")
print(message)
greet_with_parameters("NOTHING", "MAJOR")
# If you print the function call itself which is not returning anything, it would return None since all functions in Python return None by default. None is absence of the value.


def return_something():
    return "..."


print(return_something())

# Keyword argument - You can pass the name of the keyword when calling the function

# All parameter passed when defining function are required by default. You can define a default value of the parameter and it will be used even without passing in as arguments. If you pass in a different value as an argument than the one used during function definition, it will override.

# The optional parameters should ALWAYS be at the end of all required parameters.

# xargs -> variable number of arguments


# def multiply(x, y):
#     return x*y

# What if I want to add more parameters, it isn't possible. We can use * for that.

def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)
# The above function returns the list of parameters.These are called tuples. The only difference it has compared to list is that tuples cannot be modified.

# Tuples are iterables. So, you can loop over them.


# def multiply2(*iterable_tupple):
# print(iterable_tupple)

# Let's say you want to multiply all the numbers you are passing in as variable arguments (i.e Tupples)

def multiply2(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


total_value = multiply2(1, 2, 3, 4)
print(total_value)


# xxargs:
def save_user(**user):
    print(user["id"])
    print(user["name"])


# When you pass in the user as an argument with double asterik, it will be passed as a dictionary.
save_user(id=1, name="Shivang", age=29)

# Scope


def greet():
    messsage = "a"

    # message is within the scope of the function. If you try to access the variable outside of the scope of function (like message in the above example), it will throw an error "message not defined"

# Local variables have a short lifetime. When you call the functions by passing in parameter or without, python interpreter will allocate the values of the variables corresponding to that function in the memory.
# As they are not being referenced elsewhere, eventually they will be garbage collected.


# Global variable

global1 = "This is a global variable"
# Should avoid as it doesn't get garbage collector and consumes permanent memory.

# Example of overriding the global variable v/s keeping it the same.

# message = "Global variable"
# def greet():
#     message = "Local variable"
# The above message will not change the value of global variable, but if you use the keyword global in front of the message, it will.
# global message = "Changed to local variable"
