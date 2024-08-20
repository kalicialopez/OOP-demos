# Dog Class - Build Ruby using a class, as well as any other dog we want
class Dog:  # Class naming conventions; No underscores, CapitaliseEveryWord, relevant and descriptive!

    noise = "Woof!"

    @classmethod
    def create(cls, name, breed, age, fur_colour):
        """This is a class method, it gets called before the instance exists"""
        if name == "Ben":
            print("Ben is a bad name for a dog")
            name = "Alicia"
        return cls(name, breed, age, fur_colour)

    def __init__(self, name, breed, age, fur_colour):
        """this is a instance method, it gets called after the instance exists"""
        self.name = name
        self.breed = breed
        self.age = age
        self.fur_colour = fur_colour

    def info(
        self,
    ):  # A string method to represent a dog object and the attribute information about it nicely!
        return f"Dog Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Fur Color: {self.fur_colour}"

    def speak(
        self,
    ):  # We must define a bark method for our dog objects! Because that's what dogs do!
        print(self.noise)


# my_dog
# Instantiating the dog class, to create a unique instances i.e. my_dog)
my_dog = Dog("Ruby", "Staffy", 2, "Brown")

# I can access the individual attributes of my_dog with , notation
print(my_dog.breed)

# Without a string representation method defined, this will only give a reference to the object location in memory
print(my_dog.info())

# Calling the bark method to see what Ruby sounds like when she barks
my_dog.speak()


class MuteDog(Dog):
    noise = None


# my_other_dog
my_other_dog = MuteDog("Happy", "Labrador", 3, "Cream")
print(my_other_dog.info())
my_other_dog.speak()
