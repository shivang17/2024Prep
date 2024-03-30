# Let's understand the art of debugging.

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))

# In order to debug, first create the json file. For mac users, please change the settings of "Show desktop from f11 to none because this will be needed for the debugging"
# Add a breakpoint, press f5 to run the prorgam, press f10 to move to the next line of the code.
# Press f11 to enter into the function. Check for variables and in case of loop check the values being changes with each iteration within the variables section.

# For more complex programs, you can utilize the call stack.
