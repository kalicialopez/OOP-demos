# Dog Class - Build Ruby using a class, as well as any other dog we want
class Dog:  # Class naming conventions; No underscores, CapitaliseEveryWord, relevant and descriptive!

    noise = "Woof!" # Class variable aka class attribute, assigns a default VALUE to noise, for every dog object instance created

    def __init__(self, name, breed, age, fur_colour):
        """this is an instance method, it gets called after the instance exists"""
        self.name = name
        self.breed = breed
        self.age = age
        self.fur_colour = fur_colour

    def info(
        self,
    ):  # An info method to represent a dog object and the attribute information about it nicely!
        return f"Dog Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Fur Color: {self.fur_colour}"

    def speak(
        self,
    ):  # We must define a bark method for our dog objects! Because that's what dogs do!
        print(self.noise)


# my_dog
# Instantiating the dog class, to create a unique instances i.e. my_dog
dog1 = Dog("Ruby", "Staffy", 2, "Brown")
dog2 = Dog("Happy", "Golden Retriever", 3, "White")

# I can access the individual attributes of my_dog with . notation
print(dog1.breed)

# If I want all the information about our dog object
print(dog1)

# Without this info method defined, this will only give a reference to the objects location in memory
print(dog1.info())

# Calling the bark method to see what Ruby sounds like when she barks
dog1.speak()


# class MuteDog(Dog):
#     noise = None
#
#
# # my_other_dog
# my_other_dog = MuteDog("Happy", "Labrador", 3, "Cream")
# print(my_other_dog.info())
# my_other_dog.speak()
