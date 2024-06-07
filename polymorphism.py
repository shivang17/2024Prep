"""
We talked about abstract base class in the file inheritance.py. Let's learn something new on top of that

"""

from abc import ABC, abstractmethod

class UIControl(ABC):

    @abstractmethod
    def draw(self):
        pass
    #The method doesn't have anything within it's body. It's just an indication that this is an abstract method that all of it's derivatives should follow

class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("Drop down list")

# Let's also have a function call draw that takes the UIControl object and calls the draw method on it.

def draw(control):
    control.draw()

# Let's create a dropdown list object

ddl = DropDownList()
draw(ddl) #This is fine because ddl is the instance of UIControl class too since DropDownList class is derived from UIControl class. 

# So, wherever we expect the UIControl object, we can pass it's derivatives also. 
tb = TextBox()
draw(tb)

"""
    Let's understand the reason behind the above exercise. 

    imagine you want to pass the list of tuples to the draw function. let's try

    def draw(controls):
        for control in controls:
            control.draw()

draw([ddl, tb]) // It will output both values. Using this logic, you can have user interface of an application. 


Imagine we have a form with a bunch of textboxes, dropdownlist, radio buttons, etc. You can pass it in the array of tuples. 

The function will take care of rendering the entire form. 

Interesting thing is that draw doesn't know what kind of control it is working with, the rendering happens at the run time. 

Polymorphism -> Many forms (draw takes many forms depending on runtime)

"""

