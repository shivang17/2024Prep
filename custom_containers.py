# Using the standard Python data structures, let's create custom containers

class CloudTag(): #maintain the various tags on block
    def __init__(self):
        self.__tags = {}

    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) + 1

# Let's implement a scenario which returns the number of times the given tag is in the cloudtag. So, a getitem magic method will be needed

    def __getitem__(self,tag):
        return self.__tags.get(tag.lower(),0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # Length magic method

    def __len__(self):
        return len(self.__tags)
    
    # Iterator magic method using iter in-built method

    def __iter__(self):
        return iter(self.__tags)
    
cloud = CloudTag()
# print(cloud.__tags["PYTHON"])

# It is still accessible, so it is not a security settings. 

print(cloud.__dict__) #this dictionary gives all attributes {className__attribute: {}}. In this case {'_CloudTag__tags': {}}
print(cloud._CloudTag__tags)

# So, unlike java and C#, Python doesn't have a concept of private members. __ is a convention to prevent accidental access of these members. 