# Dog Class - Build Ruby using a class, as well as any other dog we want
class Dog:          # Class naming conventions; No underscores, CapitaliseEveryWord, relevant and descriptive!
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
Dog2 = Dog("Happy", "Labrador", 3, "White")
print(Dog2)
Dog2.bark()




