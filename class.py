# Class: Blueprint for creating new objects

# Object: instance of a class
 

# Examples: 

# Class: Humans
# Objects: Shivang, Yagnik , John

# Let's create a class name Point

class Point:
    # Let's create all functions related to Point. 
    def draw(self):
        print("Draw")

    # Every function needs to have at least one parameter and by convention
    # The above is the class definition, which means a blueprint to create an object of the type Point
    # Every object created using the class Point will have the Draw method

point = Point()
# Here, point will have access to the draw method
# point also has access to some of the other method, which it got access to because of inheritance. 

print(type(point))
# It will be <class '__main__.Point'> main is the module

# isinstance
print(isinstance(point, Point))

# Concept of constructor

# If we want to pass the values to point, we need to have a constructor defined within the Point class. 

class PointWithConstructor:
    def __init__(self, x,y) -> None: #init is a special method which is called as magic method. Since at least one parameter is mandatory for a function/method within the class, self is added during boilerplate itself. self is a reference to the current object
        pass

# When you call the Point class (Point(1,2)), Python will internally create Point object in memory and set self to reference the point object. The point object can also have attributes, not just methods. Attributes is the variable which include data about that object. 

# Think of attributes comparing to a human's attribute like height, color, etc and functions/methods like walk, dance, etc. 

class UnderstandConstructor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point2 = UnderstandConstructor(1,2)
print("Understand the constructor object: ", point2.x)

# Class v/s instance attributes:

# The attributes can be defined at instance level as well as class, let's understand. 

class UnderstandAttribute():
    default_color = "red"

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def draw(self):
        print(f"Point {self.a} {self.b}")

attr1 = UnderstandAttribute(1,2)
print(attr1.a)
# You can create an attribute of an instance too. For example:
attr1.c = "Custom"
print(attr1.c) #Objects in Python are dynamic

# Class level attribute will impact all instances created by the class. 

# You can change the value of class attribute outside of class as well. 
UnderstandAttribute.default_color = "Changed to yellow"
attr2 = UnderstandAttribute(3,4)
print("Color: ", attr2.default_color)

UnderstandAttribute.change_attr = "Class attribute changed"

att3 = UnderstandAttribute(5,6)
print(att3.change_attr)
# Class methods. Any method that can be defined at the class level initialization and not during the instantiation. 

# Magic methods:
# It will be called automatically by Python interpreter depending on how we use our objects and classess. 

# __init__ gets called when a new object is created using the class. So, point = Point (2,3) calls the init method. 

# Let's understand __str__ method. It will be available by default as part of the inheritance, but let's redefine it within a class to make it better. 

print("Str without defining: ", att3.__str__)

class DefineStr():
    def __init__(self,c,d):
        self.c = c
        self.d = d

    def __str__(self):
        return f"{self.c} {self.d}"
    

str1 = DefineStr("Shivang", "Suchak")
print("Str after definining", str(str1))


# Comparing two objects. 

# By default, when you compare two objects created using the same class, it will return false even if the paramaeter passed are the same. 

class CompareObj():
    def __init__(self,x,y):
        self.x = x
        self.y = y

obj1 = CompareObj(1,2)
obj2 = CompareObj(1,2)

print("Are objects equal? ", obj1 == obj2) #False, because by default it is comparing the address of the two objects, which is different since they are stored in different memory address. 

# You can define the equal memory

class CompareObj2():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x > other.x  and self.y > other.y
    
    
obj3 = CompareObj2(1,2)
obj4 = CompareObj2(1,2)
print("Did __eq__ work? ", obj3 == obj4)

# What if you want to check > or <. We can define a method for this also (Definining in the CompareObj2 class itself). Once you define the greater than logic, the less than (<) logic is also taken care of. 

obj5 = CompareObj2(5,6)
obj6 = CompareObj2(1,2)
print("Greater than?", obj5 > obj6)

obj7 = CompareObj2(3,4)
obj8 = CompareObj2(7,8)

print("Less than?", obj7 < obj8)
