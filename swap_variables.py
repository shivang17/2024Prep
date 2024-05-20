# Swap the following variables

x = 10
y = 11

# So, you want to give the value 11 to x and value 10 to y. You can createa  temp variable and assign one of the values to it

temp = x
x = y
y = temp

print("Swapped", x,y)

# However, Python has a better in-built way than to use another variable. Let's use a and b

a = 10
b = 11

a,b = b,a # Under the hood, we are just defining a tuple. a,b = (11,10)
print("New a and b", a,b)