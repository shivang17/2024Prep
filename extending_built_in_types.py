"""
    We can use inheritance even with the built-in types. Let's take an example
"""

class TextEnhancement(str):
    def duplicate(self):
        return self + self
    
text = TextEnhancement("Python")
print(text.duplicate())

# Let's extend append method of a list. 

class TrackableList(list):
    def append(self, object):
        print("append called")
        super().append(object)

list1 = TrackableList()
list1.append(1)
print(list1)
