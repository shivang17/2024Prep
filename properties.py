# There are times when you want to have control over an attribute of a class. Let's take an example

class Product:
    def __init__(self, price):
        self.price = price

    
# In above case, if you create an object using the class Product. You would want that the price of the product is in range and realistic (A negative value should not be accepted)


# For example -> price = Product(-50) will be executed by Python without any issues, but it's not correct from a practical standpoint. 

"""
    1st solution: To make the attribute "price" as private attribute by using __ and then define two methods to get and set the value of the attribute

    class Product:
        def __init__(self, price):
            self.__price = price

        def get_price(self):
            return self.__price

        def set_price(self, value):
            if value < 0:
             raise ValueError("Price cannot be negative")
            self.__price = value

    Since we have two methods in place, the constructor method should be changed to call the set method

    def __init__ (self, price):
        self.set_price(price)
"""


"""
    The above solution works but it's not "pythonic". Pythonic means to follow best practices, have a clean code, and have most of the code abstracted. 

    The above kind of code is done by someone new to Python. A better way to achieve the above result is through "property"

    A property is an object which sits in front of an attribute and allow to get and set the value of attribute. 

    Let's define a class attribute:

    # class Product:

        # price = property(get, set, del, doc). So, property is a decorator that allows to manage attribute access in a controlled and encapsulated manner. 


        price = property(get_price, set_price)

        # price can be used as a regular attribute for an instance created using the Product class. 

        # We still have access to get_price and set_price, which is polluting the class definition. 

        # You can make them private but it is not optimal. So, we can use decorators. 
        decorators -> similar to what used as @classmethod in previous files to convert the instance method to a class method. 

        We can apply property to the method

        @property
        def price(self):
            return __self.price

        @price.setter
        def set_price(self, value):
            if value < 0:
                raise ValueError ("Price cannot be zero")
            self._value = value

        


"""