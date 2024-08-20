# Parent Pet Class
class Pet:
    def __init__(self, name, breed, age, fur_colour):
        self.name = name
        self.breed = breed
        self.age = age
        self.fur_colour = fur_colour

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def petting(self):
        print(f"{self.name} is being petted.")

    def noise(self):
        print("Generic pet noise")


class Dog(Pet):
    def noise(self):
        return "Woof!"

class Cat(Pet):
    def noise(self):
        print("Meow!")


# Dogs
# Instantiating the dog class, to create unique instances i.e. Dog1 and Dog2
Dog1 = Dog("Ruby", "", 2, "Brown")
Dog2 = Dog("Happy", "Golden Retriever", 3, "White")

print(Dog2.noise())
Dog1.eat()

# Cats
# Instantiating the cat class, to create unique instances i.e. Cat1 and Cat2
Cat1 = Cat("Whiskers", "British Shorthair", 4, "Blue")
Cat2 = Cat("Sylvester", "Tabby", 5, "Orange")

Cat1.sleep()
Cat2.noise()









