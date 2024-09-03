# class method on the dog class

@classmethod
def create(cls, name, breed, age, fur_colour):
    """This is a class method, it gets called before the instance exists"""
    if name == "Ben":
        print("Ben is a bad name for a dog")
        name = "Alicia"
    return cls(name, breed, age, fur_colour)



class MuteDog(Dog):
    noise = None


# my_other_dog
my_other_dog = MuteDog("Happy", "Labrador", 3, "Cream")
print(my_other_dog.info())
my_other_dog.speak()




