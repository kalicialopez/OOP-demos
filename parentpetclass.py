# I would make function and then convert it to a method
# Then refactor it into using class values


# When we are building a class, we usually see def__init__(self, name): at the top.
# __init__ is a special method, a constructor method to be precise. It is automatically
# called anytime we instantiate a class.
# When we call init, we accept whatever is after self as the parameter name. So we need
# to pass through the name of thing you are creating i.e. the object you are instantiating

#
# What is this self keyword, and what is this code underneath it?
# Self is a way for us to define the thing. It refers to the Pet.
# It's saying this (self second line) is going to refer to the pet
# that we're going to create (or instantiate), as pet1. And I want self.name
# to equal whatever the parameter name is. And we've called it Dog.
# So that if I do dog.name down there, at run it, it's now not going to point at a
# place in memory, it's going to give me the name Dog.
# Why is it dog?

# Parent Pet Class
class Pet:          # Class naming conventions; No underscores, CapitaliseEveryWord, relevant and descriptive!
    def __init__(self, name, breed, age, fur_colour):
        self.name = name
        self.breed = breed
        self.age = age
        self.fur_colour = fur_colour

    def __str__(self):      # A string method to represent a dog object and the attribute information about it nicely!
        return f"Dog Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Fur Color: {self.fur_colour}"

    def bark(self):         # We must define a bark method for our dog objects! Because that's what dogs do!
        print("Woof!")


# Dog1
# Instantiating the dog class, to create a unique instances i.e. Dog1)
Dog1 = Dog("Ruby", "Staffy", 2, "Brown")

# I can access the individual attributes of Dog1 with , notation
print(Dog1.breed)

# Without a string representation method defined, this will only give a reference to the object location in memory
print(Dog1)

# Calling the bark method to see what Ruby sounds like when she barks
Dog1.bark()


# Dog2
Dog2 = Dog("Happy", "Labrador", 3, "Black")
print(Dog2)
Dog2.bark()

# parent pet class
class Pet:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("munch")

    def sleep(self):
        print("zzz")

    def vocalisation(self):
        print("woof")


pet1 = Pet("Dog", "Sharpei", "6")

print(pet1)     # This will print the location of this object in memory
print(pet1.name)    # This prints "Dog"










