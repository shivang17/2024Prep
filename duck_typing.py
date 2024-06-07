"""
In the example of polymorphism.py, we had a UIControl class as base class with the abstract method, draw. As it was an abstract method, every class derived from the UIControl will need to have the draw method. 

In order to achieve the polymorphism, we don't need the base class. Let us understand:

def draw(controls):
    for control in controls:
        control.draw()

In the above method, there is no requirement for the object controls to be passed coming from UIControl class. As long as an object is passed that has a draw method, it should be good. This is called duck typing (if it walks and quacks like a duck, it is a duck). 

Python is the dynamic typing language, it doesn't care about the type of object. 

However, it is a good practice to have the base class with an abstract method. This will allow to have a common contract with all the derived class and make sure the application's class built on basis of UIControl class, will all need to have draw method for consistency. 


"""