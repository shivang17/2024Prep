"""
    We understood till now that class is created to bundle the data together and create different instances out of it. 

    However, there are sometimes when there is no method within a class. For example

"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
p1 = Point(1,2)
p2 = Point(1,2)

print(p1 == p2) # This will return False since the memory at which p1 and p2 are stored is different. 

#If we want to have a value comparison, we need to define a method within the class


class Equality:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

e1 = Equality(1,2)
e2 = Equality(1,2)

print(e1 == e2)

# In above case, we had to manually create a method to have that equality by value, but in general if you are dealing with class that only has data and no methods, we can use namedtuple from the collections object. 

from collections import namedtuple

Point = namedtuple("Distance", ["x", "y"])

p3 = Point(x=1, y=2)
p4 = Point(x = 1, y = 2)
print(p3 == p4)

# namedtuple is better in this case because it's cleaner data, better tuple as they have attributes just like class. p.s -> they are immutable

# For example, in the above code, p3.x is 1, but if you try to set as p3.x = 5, it will throw an error. 