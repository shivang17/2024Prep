# Inheritance is a very known concept in OOP where a child class can be inherited from Parent to share/access the properties

# For example, we have a class Mammal. All mammals will eat and walk. So, let's create those methods:

"""class Mammal:
    def eat(self):
        print("eat")
    
    def walk(self):
        print("walk")

# Let's say we have another class Fish.

class Fish:
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")

# We are seeing two methods eat being repeated in the two class. So, let's create a parent class Animal and include the methods which we can repatedly use instead of defining in all the classes which can have the respective methods. This is the programming principle called DRY (Don't Repeat Yourself)
"""


class Animal:
    def __init__(self):
        self.weight = 4

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.age = 2
        # We can call super class after initializing/overriding the variable as well. 

    def walk(self,a):
        print("walk")
        self.a = a

class Fish:
    def swim(self):
        print("swim")

mammal = Mammal()
print(mammal.weight)

# Avoid multi-level inheritance. For example, Employee is a person which is a livingCreature which is a Thing, we should not have classess like this. 


# Multiple inheritance:

# If a class has multiple base class, if two base class has the same method, it will execute the method of the one passed during the class definition of the sub class. Let's take an example

class Employee:
    def greet(self):
        print("employee greet")


class Person:
    def greet(self):
        print("person greet")

class Manager(Employee,Person):
    pass

manager = Manager()

print(manager.greet())

"""
    Good example of inheritance:
        Let's say you want to read a stream of data. The medium can be different, it can be through a file, network, or memory. 

        So, we can have Stream as the base class which has ability to open and close the file and then derived class which will have the ability to read based on the type


"""

class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        # You would not want to open an already opened file. So, check if the file is open. If yes,then throw an exception. Here, we will need to have a custom exception because none of the built-in ones are applicable here.
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened= True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

# The above is a good example of inheritance because of only two derived class and not multi-level inheritance nor multiple inheritance. 

# BUT there is a problem here. We can create a stream object and call open method, which doesn't sound intuitive since the open and close phenomenon is for specifc stream source (file or network). 

# So, we shouldn't be able to create an instance of the base class. We should always create the sub class and then create an instance of the sub class. 


# We only created Stream class as the base class to provide some base code to be used across different streams. 
# File and Network stream has both read, but it needs to be consistent if we create one more class of stream

# We should enforce the common interface across different kind of streams. That's when we will use abstract base class. 

# An abstract base class is like a half baked cookie. It's goal is to provide common code to these derivatives. 

# The abstract class implementation will be done as follows:

from abc import ABC, abstractmethod #abc -> abstract base class
"""
     
class Stream(ABC):

    ...

    @abstractmethod
    def read(self):
        pass

        We cannot create instance of an abstract class. If a class is derived from an abstract class, it should have the abstract method defined in the abstract class, otherwise it will not allow to create the instance (otherwise it will remain abstract and not concrete)

"""




