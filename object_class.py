# All class in Python derives from object class. Let's take the example of Animal and Mammal from the previous file

from inheritance import Mammal, Animal

m = Mammal()

print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))

print(isinstance(Animal, object))

# Another method that might be helpful will be issubclass

print(issubclass(Mammal, Animal))